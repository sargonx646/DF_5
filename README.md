# DecisionForge

Simulate organizational and policy decision-making with agentic AI.

## Deployment

1. Copy `.env.example` to `.env` and fill in your `OPENROUTER_API_KEY`.
2. Push this repo to GitHub.
3. On Streamlit Cloud, create a new app from this GitHub repo.
4. The `Procfile` and `requirements.txt` are configured for seamless deployment.

## Local Run

```bash
pip install -r requirements.txt
cp .env.example .env
streamlit run app.py
```