from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

analyzer = SentimentIntensityAnalyzer()

def analyze_message_sentiment(text):
    """
    Returns (label, score). Label is Positive/Neutral/Negative.
    Score is the compound score in [-1,1].
    """
    vs = analyzer.polarity_scores(text)
    c = vs["compound"]
    if c >= 0.05:
        label = "Positive"
    elif c <= -0.05:
        label = "Negative"
    else:
        label = "Neutral"
    return label, round(c, 4)

def analyze_sentiment_scores(messages):
    """
    messages: list of strings (user messages).
    Returns (overall_label, average_score, stats)
    stats: {positive, neutral, negative, total}
    """
    if not messages:
        return "Neutral", 0.0, {"positive":0, "neutral":0, "negative":0, "total":0}

    scores = []
    positive = neutral = negative = 0
    for m in messages:
        label, score = analyze_message_sentiment(m)
        scores.append(score)
        if label == "Positive":
            positive += 1
        elif label == "Negative":
            negative += 1
        else:
            neutral += 1

    avg = sum(scores) / len(scores)
    if avg >= 0.05:
        overall = "Positive"
    elif avg <= -0.05:
        overall = "Negative"
    else:
        overall = "Neutral"

    stats = {"positive": positive, "neutral": neutral, "negative": negative, "total": len(messages)}
    return overall, round(avg,4), stats
