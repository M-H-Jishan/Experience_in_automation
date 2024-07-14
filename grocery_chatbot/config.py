import os
from dotenv import load_dotenv

load_dotenv()

DATABASE_URI = os.getenv('DATABASE_URI')
STRIPE_API_KEY = os.getenv('STRIPE_API_KEY')