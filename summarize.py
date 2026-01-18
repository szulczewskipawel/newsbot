import requests
import os

OLLAMA_URL = "http://localhost:11434/api/generate"

PROMPT_TEMPLATE = """
Streść poniższy artykuł w maksymalnie 5 krótkich punktach.
Pisz po polsku, rzeczowo, bez opinii i emocjonalnych określeń.

Artykuł:
{content}
"""

def summarize(content):
    prompt = PROMPT_TEMPLATE.format(content=content)

    response = requests.post(
        OLLAMA_URL,
        json={"model": "qwen2.5-coder:7b", "prompt": prompt, "stream": False},
        timeout=300
    )

    return response.json().get("response", "").strip()

