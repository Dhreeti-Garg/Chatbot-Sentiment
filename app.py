import json
import os
from flask import Flask, render_template, request, jsonify
from sentiment_analysis import analyze_message_sentiment, analyze_sentiment_scores

app = Flask(__name__)
DATA_FILE = "conversation.json"

# Load or initialize conversation storage
if os.path.exists(DATA_FILE):
    try:
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            conversation = json.load(f)
    except Exception:
        conversation = []
else:
    conversation = []

def save_conversation():
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(conversation, f, ensure_ascii=False, indent=2)

# Improved rule-based reply logic (expandable)
def bot_reply(user_text):
    text = user_text.lower().strip()
    # greetings
    if any(tok in text for tok in ["hi", "hello", "hey", "good morning", "good afternoon"]):
        return "Hi — I’m Lumi, your assistant. I can answer questions, provide suggestions, and analyze mood. How can I help you today?"
    # identity
    if "who are you" in text or "your name" in text or "what are you" in text:
        return "I’m Lumi — a lightweight assistant built for demos. I analyze the sentiment of conversations and help with basic queries."
    # capabilities
    if "help" in text or "can you" in text or "what can you do" in text:
        return ("I can: 1) chat with you naturally; 2) analyze sentiment per message and for the whole conversation; "
                "3) show a mood trend graph; and 4) provide a final sentiment report. Try asking me something!")
    # thanks
    if any(w in text for w in ["thanks", "thank you", "thx"]):
        return "You’re welcome — happy to help! Anything else?"
    # goodbye
    if any(w in text for w in ["bye", "goodbye", "see you", "quit"]):
        return "Goodbye! If you want to start fresh, click Reset."
    # requests for examples
    if "example" in text or "show" in text and "example" in text:
        return "Try asking: 'I had a bad day at work' or 'I love this product' — I'll analyze the sentiment for each message."
    # ask for clarification if too short
    if len(text.split()) <= 2 and any(c.isalpha() for c in text):
        return "Could you please elaborate a bit more so I can assist you better?"
    # fallback: echo + suggest clarification
    return "Thanks — I got that. Could you give a bit more detail or ask a specific question so I can respond more precisely?"

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    data = request.json or {}
    user_message = data.get("message", "").strip()
    if not user_message:
        return jsonify({"error": "Empty message"}), 400

    bot_message = bot_reply(user_message)
    sentiment_label, sentiment_score = analyze_message_sentiment(user_message)

    entry = {
        "user": user_message,
        "bot": bot_message,
        "sentiment": sentiment_label,
        "score": sentiment_score
    }
    conversation.append(entry)
    save_conversation()
    return jsonify(entry)

@app.route("/sentiment", methods=["GET"])
def sentiment():
    user_texts = [c["user"] for c in conversation]
    overall_label, avg_score, stats = analyze_sentiment_scores(user_texts)
    response = {
        "overall_label": overall_label,
        "average_score": avg_score,
        "stats": stats,
        "conversation": conversation
    }
    return jsonify(response)

@app.route("/reset", methods=["POST"])
def reset():
    global conversation
    conversation = []
    save_conversation()
    return jsonify({"status": "ok", "message": "Conversation reset."})

if __name__ == "__main__":
    app.run(debug=True)
