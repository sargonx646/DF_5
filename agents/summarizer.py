from config import OPENROUTER_API_KEY, API_URL, MODEL_NAME
import requests

def summarize_and_analyze(transcript):
    prompt = "Summarize the following debate and highlight consensus and conflicts:\n" + str(transcript)
    response = requests.post(
        API_URL,
        headers={ "Authorization": f"Bearer {OPENROUTER_API_KEY}", "Content-Type": "application/json" },
        json={ "model": MODEL_NAME, "messages":[{"role":"user","content":prompt}] }
    )
    data = response.json()
    summary = data["choices"][0]["message"]["content"] if "choices" in data else "Error"
    # Extract keywords naively
    keywords = [w.strip().lower() for w in summary.split() if len(w)>4][:20]
    return summary, keywords