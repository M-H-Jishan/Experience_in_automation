import os
from dotenv import load_dotenv

load_dotenv()

DATABASE_URI = os.getenv("DATABASE_URI", "sqlite:///grocery.db")
STRIPE_API_KEY = os.getenv("STRIPE_API_KEY", "")
PORT = int(os.getenv("PORT", 5000))
DEBUG = os.getenv("DEBUG", "False").lower() == "true"
