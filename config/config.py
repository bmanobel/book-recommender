import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

GROK_API_KEY = os.getenv("GROK_API_KEY")
MODEL_NAME = "llama-3.1-8b-instant"
