import os
from dotenv import load_dotenv

load_dotenv()
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")
MODEL_NAME = "openai/gpt-3.5-turbo"
API_URL = "https://openrouter.ai/api/v1/chat/completions"