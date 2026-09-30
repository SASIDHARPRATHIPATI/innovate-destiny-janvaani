# Janvaani Backend

Flask API that uses Google Gemini to analyze citizen feedback.

## Setup

1. Install dependencies:
   pip install -r requirements.txt

2. Set your Gemini API key:
   - Get one at https://aistudio.google.com/apikey
   - Copy .env.example to .env and paste your key

3. Run:
   python app.py

4. Open http://localhost:8080

## Endpoints

- GET  /              → Frontend UI
- GET  /health        → Health check
- POST /api/submit    → Analyze feedback with Gemini
