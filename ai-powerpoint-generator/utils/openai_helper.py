import os
import openai
from dotenv import load_dotenv

def set_openai_api_key():
    load_dotenv()
    openai.api_key = os.getenv("OPENAI_API_KEY")
    if not openai.api_key:
        raise ValueError("OpenAI API key not found. Please set it in the .env file.")