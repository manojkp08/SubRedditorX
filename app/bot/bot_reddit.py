import praw

class RedditBot:
    def __init__(self, client_id, client_secret, username, password, user_agent):
        self.reddit = praw.Reddit(
            client_id=client_id,
            client_secret=client_secret,
            username=username,
            password=password,
            user_agent=user_agent,
        )

    def post_to_subreddit(self, subreddit_name, title, content):
        subreddit = self.reddit.subreddit(subreddit_name)
        subreddit.submit(title, selftext=content)

    def comment_on_post(self, post_url, comment_text):
        submission = self.reddit.submission(url=post_url)
        submission.reply(comment_text)

    def like_post(self, post_url):
        submission = self.reddit.submission(url=post_url)
        submission.upvote()
