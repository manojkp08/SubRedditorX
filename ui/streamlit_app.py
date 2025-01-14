import streamlit as st
from bot_reddit import RedditBot
from bot_x import TwitterBot
from db_handler import DBHandler
from config import *

# Initialize bots and database handler
reddit_bot = RedditBot(REDDIT_CLIENT_ID, REDDIT_CLIENT_SECRET, REDDIT_USERNAME, REDDIT_PASSWORD, REDDIT_USER_AGENT)
twitter_bot = TwitterBot(TWITTER_API_KEY, TWITTER_API_SECRET, TWITTER_ACCESS_TOKEN, TWITTER_ACCESS_TOKEN_SECRET)
db_handler = DBHandler()

# Streamlit UI
st.title("Reddit & X Bot Automation")
st.sidebar.header("Actions")

# Reddit Section
st.subheader("Reddit Automation")
reddit_action = st.selectbox("Select an action", ["Post to Subreddit", "Comment on Post", "View Logs"])
if reddit_action == "Post to Subreddit":
    subreddit_name = st.text_input("Subreddit Name")
    title = st.text_input("Post Title")
    content = st.text_area("Post Content")
    if st.button("Submit Post"):
        reddit_bot.post_to_subreddit(subreddit_name, title, content)
        db_handler.log_to_mongo("reddit", "post", {"subreddit": subreddit_name, "title": title})
        st.success("Post submitted!")
elif reddit_action == "Comment on Post":
    post_url = st.text_input("Post URL")
    comment_text = st.text_area("Comment Text")
    if st.button("Submit Comment"):
        reddit_bot.comment_on_post(post_url, comment_text)
        db_handler.log_to_mongo("reddit", "comment", {"post_url": post_url, "comment_text": comment_text})
        st.success("Comment submitted!")
elif reddit_action == "View Logs":
    logs = db_handler.fetch_logs("reddit")
    st.json(logs)

# Twitter Section
st.subheader("X Automation")
twitter_action = st.selectbox("Select an action", ["Post a Tweet", "Like a Tweet", "Retweet", "View Logs"])
if twitter_action == "Post a Tweet":
    content = st.text_area("Tweet Content")
    if st.button("Post Tweet"):
        twitter_bot.post_tweet(content)
        db_handler.log_to_mongo("twitter", "post", {"content": content})
        st.success("Tweet posted!")
elif twitter_action == "Like a Tweet":
    tweet_id = st.text_input("Tweet ID")
    if st.button("Like Tweet"):
        twitter_bot.like_tweet(tweet_id)
        db_handler.log_to_mongo("twitter", "like", {"tweet_id": tweet_id})
        st.success("Tweet liked!")
elif twitter_action == "Retweet":
    tweet_id = st.text_input("Tweet ID")
    if st.button("Retweet"):
        twitter_bot.retweet(tweet_id)
        db_handler.log_to_mongo("twitter", "retweet", {"tweet_id": tweet_id})
        st.success("Retweeted!")
elif twitter_action == "View Logs":
    logs = db_handler.fetch_logs("twitter")
    st.json(logs)
