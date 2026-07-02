import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

_client = None
if os.getenv("OPENAI_API_KEY"):
    _client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def get_client() -> OpenAI:
    if not _client:
        raise ValueError("OPENAI_API_KEY not found. Please set it in the .env file.")
    return _client
