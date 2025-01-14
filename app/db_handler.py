from pymongo import MongoClient
import redis
import json
from config import MONGO_URI, REDIS_HOST, REDIS_PORT

class DBHandler:
    def __init__(self):
        # MongoDB Setup
        self.mongo_client = MongoClient(MONGO_URI)
        self.mongo_db = self.mongo_client["bot_logs"]
        self.reddit_logs = self.mongo_db["reddit_logs"]
        self.twitter_logs = self.mongo_db["twitter_logs"]

        # Redis Setup
        self.redis_client = redis.StrictRedis(host=REDIS_HOST, port=REDIS_PORT, decode_responses=True)

    def log_to_mongo(self, platform, action, details):
        log = {"platform": platform, "action": action, "details": details}
        if platform == "reddit":
            self.reddit_logs.insert_one(log)
        elif platform == "twitter":
            self.twitter_logs.insert_one(log)

    def cache_to_redis(self, key, value, ttl=3600):
        self.redis_client.set(key, json.dumps(value), ex=ttl)

    def fetch_from_redis(self, key):
        data = self.redis_client.get(key)
        return json.loads(data) if data else None

    def fetch_logs(self, platform):
        if platform == "reddit":
            return list(self.reddit_logs.find())
        elif platform == "twitter":
            return list(self.twitter_logs.find())
        return []
