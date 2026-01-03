import os
from dotenv import load_dotenv

# Force-load .env from the project root
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ENV_PATH = os.path.join(BASE_DIR, ".env")

load_dotenv(ENV_PATH, override=True)

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
SERPAPI_KEY = os.getenv("SERPAPI_KEY")
HF_TOKEN = os.getenv("HF_TOKEN")

# Constants
MODEL_ID = "mistralai/Mistral-7B-Instruct-v0.3"
MAX_TOKENS = 2048
TEMPERATURE = 0.7
APP_TITLE = "🌍 AI Travel Planner"
