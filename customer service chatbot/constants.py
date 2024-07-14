# constants.py
import os
from dotenv import load_dotenv
try:
    load_dotenv()
except UnicodeDecodeError:
    print("Warning: Could not load .env file due to encoding issues.")

APIKEY = os.getenv("OPENAI_API_KEY")

if not APIKEY:
    raise ValueError("No API key set for OpenAI. Please check your .env file or environment variables.")