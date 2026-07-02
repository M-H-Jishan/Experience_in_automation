import os
from dotenv import load_dotenv

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "")
OPENAI_MODEL = os.getenv("OPENAI_MODEL", "gpt-3.5-turbo")
KNOWLEDGE_BASE_PATH = os.getenv(
    "KNOWLEDGE_BASE_PATH",
    os.path.join(os.path.dirname(os.path.abspath(__file__)), "knowledge_base", "Data.txt"),
)
PORT = int(os.getenv("PORT", 5000))
DEBUG = os.getenv("DEBUG", "False").lower() == "true"
