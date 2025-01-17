from pymongo import MongoClient
from config import MONGO_URI

class DBHandler:
    def __init__(self):
        # MongoDB Setup
        self.mongo_client = MongoClient(MONGO_URI)
        self.mongo_db = self.mongo_client["bot_logs"]
        self.reddit_logs = self.mongo_db["reddit_logs"]

    def log_to_mongo(self, platform, action, details):
        log = {"platform": platform, "action": action, "details": details}
        if platform == "reddit":
            self.reddit_logs.insert_one(log)

    def fetch_logs(self, platform):
        if(platform == "reddit"):
            return list(self.reddit_logs.find())
        return []
