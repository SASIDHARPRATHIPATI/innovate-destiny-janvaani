"""
Janvaani - Voice of the People
Team Innovate Destiny | Track 1

Flask API for citizen feedback aggregation.
"""

from flask import Flask, request, jsonify, send_from_directory
from gemini_client import analyze_feedback
import os

app = Flask(__name__, static_folder='../frontend', static_url_path='')


@app.route('/')
def home():
    return send_from_directory(app.static_folder, 'index.html')


@app.route('/health')
def health():
    return jsonify({
        "project": "Janvaani",
        "team": "Innovate Destiny",
        "track": "Track 1 - AI for Digital Public Infrastructure & Governance",
        "status": "running"
    })


@app.route('/api/submit', methods=['POST'])
def submit_feedback():
    """Accept citizen feedback and analyze it with Gemini."""
    data = request.get_json()

    if not data or not data.get('text'):
        return jsonify({"error": "No text provided"}), 400

    text = data.get('text', '').strip()
    language = data.get('language', 'auto')

    result = analyze_feedback(text, language)
    return jsonify(result)


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8080))
    app.run(host='0.0.0.0', port=port, debug=True)
