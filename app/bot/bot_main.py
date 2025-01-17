from bot.bot_reddit import RedditBot
from config import *

# Initialize bots
reddit_bot = RedditBot(REDDIT_CLIENT_ID, REDDIT_CLIENT_SECRET, REDDIT_USERNAME, REDDIT_PASSWORD, REDDIT_USER_AGENT)

def main():
    # Reddit Example
    reddit_bot.post_to_subreddit("test", "Hello World", "This is a test post.")
    reddit_bot.comment_on_post("https://www.reddit.com/r/test/comments/example", "This is a test comment.")
    reddit_bot.like_post("https://www.reddit.com/r/test/comments/example")

if __name__ == "__main__":
    main()
