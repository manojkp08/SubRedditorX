from bot_reddit import RedditBot
from bot_x import TwitterBot
from config import *

# Initialize bots
reddit_bot = RedditBot(REDDIT_CLIENT_ID, REDDIT_CLIENT_SECRET, REDDIT_USERNAME, REDDIT_PASSWORD, REDDIT_USER_AGENT)
twitter_bot = TwitterBot(TWITTER_API_KEY, TWITTER_API_SECRET, TWITTER_ACCESS_TOKEN, TWITTER_ACCESS_TOKEN_SECRET)

def main():
    # Reddit Example
    reddit_bot.post_to_subreddit("test", "Hello World", "This is a test post.")
    reddit_bot.comment_on_post("https://www.reddit.com/r/test/comments/example", "This is a test comment.")

    # Twitter Example
    twitter_bot.post_tweet("Hello, Twitter!")
    twitter_bot.like_tweet(1234567890)  # Replace with a real tweet ID
    twitter_bot.retweet(1234567890)    # Replace with a real tweet ID

if __name__ == "__main__":
    main()
