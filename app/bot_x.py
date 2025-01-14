import tweepy

class TwitterBot:
    def __init__(self, api_key, api_secret, access_token, access_token_secret):
        auth = tweepy.OAuth1UserHandler(api_key, api_secret, access_token, access_token_secret)
        self.api = tweepy.API(auth)

    def post_tweet(self, content):
        self.api.update_status(content)

    def like_tweet(self, tweet_id):
        self.api.create_favorite(tweet_id)

    def retweet(self, tweet_id):
        self.api.retweet(tweet_id)
