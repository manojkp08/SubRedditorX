import os
from dotenv import load_dotenv

load_dotenv()

# Reddit API Credentials
REDDIT_CLIENT_ID = os.getenv("REDDIT_CLIENT_ID")
REDDIT_CLIENT_SECRET = os.getenv("REDDIT_CLIENT_SECRET")
REDDIT_USERNAME = os.getenv("REDDIT_USERNAME")
REDDIT_PASSWORD = os.getenv("REDDIT_PASSWORD")
REDDIT_USER_AGENT = os.getenv("REDDIT_USER_AGENT")

# MongoDB and Redis Config
MONGO_URI = os.getenv("MONGO_URI")

# Gemini API Credentials
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")