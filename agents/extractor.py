import json
import requests
from config import OPENROUTER_API_KEY, API_URL, MODEL_NAME

def extract_info(dilemma, process_hint):
    prompt = f"""You are an AI analyst.
Extract key stakeholders, issues, and the decision-making steps.
Return only JSON with keys: stakeholders, issues, process.

Dilemma: {dilemma}
Process Hint: {process_hint}
"""
    response = requests.post(
        API_URL,
        headers={ "Authorization": f"Bearer {OPENROUTER_API_KEY}", "Content-Type": "application/json" },
        json={ "model": MODEL_NAME, "messages": [{"role":"user","content":prompt}] }
    )
    data = response.json()
    if "choices" in data:
        try:
            return json.loads(data["choices"][0]["message"]["content"])
        except json.JSONDecodeError:
            return {"error": "Invalid JSON", "raw": data["choices"][0]["message"]["content"]}
    return {"error": data.get("error", "Unknown error"), "raw": data}