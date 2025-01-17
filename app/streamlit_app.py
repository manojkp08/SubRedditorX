import streamlit as st
from bot.bot_reddit import RedditBot
from db.db_handler import DBHandler
from config import *
from gemini_api import generate_content

# Page configuration
st.set_page_config(
    page_title="Reddit Bot Automation",
    page_icon="🤖",
    layout="wide"
)

# Custom CSS
st.markdown("""
    <style>
    .stButton>button {
        width: 100%;
        background-color: #ff4500;
        color: white;
    }
    .stButton>button:hover {
        background-color: #ff5722;
    }
    .main-header {
        color: #ff4500;
        text-align: center;
        font-size: 2.5rem;
        margin-bottom: 2rem;
    }
    .subheader {
        color: #1a1a1b;
        margin-bottom: 1rem;
    }
    .stTextInput>div>div>input {
        border-radius: 5px;
    }
    .stTextArea>div>div>textarea {
        border-radius: 5px;
    }
    </style>
""", unsafe_allow_html=True)

# Initialize bots and database handler
reddit_bot = RedditBot(REDDIT_CLIENT_ID, REDDIT_CLIENT_SECRET, REDDIT_USERNAME, REDDIT_PASSWORD, REDDIT_USER_AGENT)
db_handler = DBHandler()

# Main title with Reddit styling
st.markdown("<h1 class='main-header'>🤖 Reddit Bot Automation</h1>", unsafe_allow_html=True)

# Sidebar
with st.sidebar:
    st.image("app/reddit-logo.png", width=100)
    st.markdown("### 🎯 Actions")
    st.markdown("---")
    reddit_action = st.radio(
        "",
        ["Post to Subreddit", "Comment on Post", "View Logs"]
    )

# Main content area
if reddit_action == "Post to Subreddit":
    st.markdown("<h2 class='subheader'>📝 Create New Post</h2>", unsafe_allow_html=True)
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        with st.form("post_form"):
            post_type = st.select_slider(
                "Select Post Type",
                options=["Manual Post", "Post with GenAI"]
            )
            
            if post_type == "Manual Post":
                subreddit_name = st.text_input("🔍 Subreddit Name", placeholder="e.g., Python")
                title = st.text_input("📋 Post Title", placeholder="Enter your post title")
                content = st.text_area("✏️ Post Content", height=200, placeholder="Write your post content here...")
                submit_button = st.form_submit_button("Submit Post")
                
                if submit_button:
                    if subreddit_name and title and content:
                        reddit_bot.post_to_subreddit(subreddit_name, title, content)
                        db_handler.log_to_mongo("reddit", "post", {"subreddit": subreddit_name, "title": title})
                        st.success("✅ Post submitted successfully!")
                    else:
                        st.error("❌ Please fill in all required fields")
            
            else:  # Post with GenAI
                subreddit_name = st.text_input("🔍 Subreddit Name", placeholder="e.g., Python")
                prompt = st.text_input("🤖 AI Prompt", placeholder="Enter your prompt for AI-generated content")
                submit_button = st.form_submit_button("Generate & Post")
                
                if submit_button:
                    if subreddit_name and prompt:
                        with st.spinner("Generating content..."):
                            generated_content = generate_content(prompt)
                            title, content = generated_content.split("\n", 1)
                            reddit_bot.post_to_subreddit(subreddit_name, title, content)
                            db_handler.log_to_mongo("reddit", "post", {"subreddit": subreddit_name, "title": title})
                        st.success("✅ AI-generated post submitted successfully!")
                        with st.expander("View Generated Content"):
                            st.markdown("**Title:**")
                            st.info(title)
                            st.markdown("**Content:**")
                            st.info(content)
                    else:
                        st.error("❌ Please provide both subreddit name and prompt")
    
    with col2:
        st.info("""
        ### 📌 Posting Guidelines
        
        - Ensure your post follows subreddit rules
        - Use clear and descriptive titles
        - Format your content appropriately
        - Be respectful and authentic
        """)

elif reddit_action == "Comment on Post":
    st.markdown("<h2 class='subheader'>💬 Add Comment</h2>", unsafe_allow_html=True)
    
    with st.form("comment_form"):
        comment_type = st.select_slider(
            "Select Comment Type",
            options=["Manual Comment", "Comment with GenAI"]
        )
        
        post_url = st.text_input("🔗 Post URL", placeholder="Enter the Reddit post URL")
        
        if comment_type == "Manual Comment":
            comment_text = st.text_area("✏️ Comment Text", height=150, placeholder="Write your comment here...")
        else:
            comment_text = st.text_input("🤖 AI Prompt", placeholder="Enter prompt for AI-generated comment")
            
        submit_button = st.form_submit_button("Submit Comment")
        
        if submit_button:
            if post_url and comment_text:
                if comment_type == "Comment with GenAI":
                    with st.spinner("Generating comment..."):
                        comment_text = generate_content(comment_text)
                reddit_bot.comment_on_post(post_url, comment_text)
                db_handler.log_to_mongo("reddit", "comment", {"post_url": post_url, "comment_text": comment_text})
                st.success("✅ Comment submitted successfully!")
                if comment_type == "Comment with GenAI":
                    with st.expander("View Generated Comment"):
                        st.info(comment_text)
            else:
                st.error("❌ Please fill in all required fields")

elif reddit_action == "View Logs":
    st.markdown("<h2 class='subheader'>📊 Activity Logs</h2>", unsafe_allow_html=True)
    
    logs = db_handler.fetch_logs("reddit")
    
    # Create tabs for different log types
    post_logs = [log for log in logs if log['action'] == 'post']
    comment_logs = [log for log in logs if log['action'] == 'comment']
    
    tab1, tab2 = st.tabs(["📝 Posts", "💬 Comments"])
    
    with tab1:
        if post_logs:
            for log in post_logs:
                with st.expander(f"Post in r/{log['details']['subreddit']}"):
                    st.write(f"**Title:** {log['details']['title']}")
                    st.write(f"**Time:** {log.get('timestamp', 'N/A')}")
        else:
            st.info("No post logs available")
    
    with tab2:
        if comment_logs:
            for log in comment_logs:
                with st.expander(f"Comment on {log['details']['post_url']}"):
                    st.write(f"**Comment:** {log['details']['comment_text']}")
                    st.write(f"**Time:** {log.get('timestamp', 'N/A')}")
        else:
            st.info("No comment logs available")