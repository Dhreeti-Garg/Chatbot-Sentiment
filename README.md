# SmartAssist — Sentiment-Aware Chatbot (Assignment-ready)

## Overview
SmartAssist is an interactive chatbot built with **Flask** and **VADER** sentiment analysis. It implements:
- **Tier 1**: Conversation-level sentiment (final report)
- **Tier 2**: Statement-level sentiment (per message)
- Live mood trend chart and conversation statistics

## Features
- Clean ChatGPT-style UI (modern, responsive)
- Per-message sentiment labels + emoji
- Numeric sentiment scores (VADER compound)
- Trend chart (Chart.js)
- Conversation persistence (`conversation.json`)
- Reset endpoint for testing

## Tech stack
- Python (Flask)
- VADER Sentiment (`vaderSentiment`)
- HTML / CSS / JS (Chart.js)

## Run locally
1. Install dependencies:
   ```bash
   pip install -r requirements.txt
