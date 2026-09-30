"""
Gemini Client - Multilingual feedback analysis for Janvaani.
Team Innovate Destiny | Track 1
"""

import os
import json
import google.generativeai as genai

genai.configure(api_key=os.environ.get("GEMINI_API_KEY"))

model = genai.GenerativeModel('gemini-1.5-pro')


PROMPT_TEMPLATE = '''
You are Janvaani, an AI assistant for India's Digital Public Infrastructure.

Analyze the following citizen feedback and return ONLY valid JSON with these keys:
- "translation": English translation of the feedback
- "category": one of [Road, Water, Health, Education, Electricity, Sanitation, Other]
- "location": extracted village/district/state (or "unknown")
- "urgency": integer from 1 to 10
- "summary": one-line summary in English

Citizen feedback: {text}

Return ONLY the JSON object. No explanations, no markdown.
'''


def analyze_feedback(text: str, language: str = "auto") -> dict:
    """Analyze citizen feedback using Google Gemini."""
    prompt = PROMPT_TEMPLATE.format(text=text)

    try:
        response = model.generate_content(prompt)
        raw = response.text.strip()

        # Clean markdown fences if Gemini wraps it
        if raw.startswith('`'):
            raw = raw.split('`')[1]
            if raw.startswith('json'):
                raw = raw[4:]
        raw = raw.strip()

        parsed = json.loads(raw)
        return {
            "success": True,
            "input": text,
            "language": language,
            "analysis": parsed
        }
    except Exception as e:
        return {
            "success": False,
            "input": text,
            "error": str(e)
        }
