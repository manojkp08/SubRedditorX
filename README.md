# 🤖 SubRedditorX

<div align="center">
  <img src="app/reddit-logo.png" alt="Reddit Bot Logo" width="200" />
  <br>
  <h3>🚀 AI-Powered Reddit Automation</h3>
  <p>A robust automated Reddit bot built with Python that can post, upvote, and comment on any subreddit through a single GenAI prompt interface without manual Reddit navigation.</p>
</div>

---

## ✨ Features

- 🧠 **AI-Powered Interaction**: Use Gemini AI to generate and process Reddit interactions
- 🔄 **Multiple Actions**: Post new content, upvote posts, and comment on threads
- 🖥️ **Simple Interface**: Streamlit web interface for easy interaction
- 📊 **Activity Tracking**: MongoDB integration for comprehensive activity logging
- 🌐 **Automated Browser Control**: Selenium for headless Reddit interaction

## 🛠️ Tech Stack

- 🐍 Python
- 📊 Streamlit (UI)
- 🧠 Gemini API (AI capabilities)
- 🔍 Selenium (browser automation)
- 🗄️ MongoDB (activity logging)

## 📥 Installation

```bash
# Clone the repository
git clone https://github.com/manojkp08/SubRedditorX.git
cd SubRedditorX

# Install dependencies
pip install -r requirements.txt

# Set up environment variables
cp .env.example .env
# Edit .env with your API keys and credentials
```

## ⚙️ Configuration

Before running the bot, update the following in your `.env` file:

```
GEMINI_API_KEY=your_gemini_api_key
REDDIT_USERNAME=your_reddit_username
REDDIT_PASSWORD=your_reddit_password
REDDIT_CLIENT_ID=your_reddit_client_id
REDDIT_CLIENT_SECRET=your_reddit_client_secret
MONGODB_URI=your_mongodb_connection_string
```

## 🚀 Usage

```bash
# Start the Streamlit interface
streamlit run app/streamlit_app.py
```

## 📸 Screenshots

<div align="center">
  <img src="https://github.com/user-attachments/assets/17745544-f90f-4ef1-b853-89ca6a74aacc" width="600" />
  <p><i>Create a post manually !!</i></p>
  
  <img src="https://github.com/user-attachments/assets/28b063b4-0b7d-4b8c-b916-9d900fb27937" width="600" />
  <p><i>Create a post using GenAI !!</i></p>
  
  <img src="https://github.com/user-attachments/assets/0ae4f902-6c6d-4e1a-aeb8-89ca5aeb2b12" width="600" />
  <p><i>Generate a comment !!</i></p>
  
  <img src="https://github.com/user-attachments/assets/93812dac-3689-4692-ab66-ff21cd149301" width="600" />
  <p><i>Example Usage on Reddit's website !!</i></p>
</div>

## 📝 Interface Guide

1. 🎯 **Select Action**: Choose to post, comment, or upvote
2. 🔍 **Target Selection**: Enter subreddit name or post URL
3. 💬 **AI Prompt**: Enter your natural language prompt for the AI to process
4. ▶️ **Execute**: Bot will perform the requested action on Reddit
5. 📋 **View Logs**: Check the history of all bot actions

## 📁 Project Structure

```
SUBREDDITORX/
├── .vscode/
├── app/
│   ├── **pycache**/
│   ├── bot/
│   ├── db/
│   ├── config.py
│   ├── gemini_api.py
│   ├── reddit-logo.png
│   ├── streamlit_app.py
│   ├── test.py
│   └── utils.py
├── ui_automation/ (under development phase)
├── .env (you have to add your own)
├── .gitignore
├── docker-compose.yml
├── Dockerfile
├── README.md
└── requirements.txt
```

## ⚠️ Limitations

- ⏱️ Respects Reddit's rate limiting and terms of service
- 🔐 Requires valid Reddit credentials
- 📊 Gemini API usage subject to quota limitations

## 📢 Disclaimer

This tool is intended for legitimate Reddit engagement. Users are responsible for adhering to Reddit's terms of service and content policies.

---

<div align="center">
  <p>⭐ Star this repository if you find it useful! ⭐</p>
  <p>Made with ❤️ by <a href="https://github.com/manojkp08">manojkp08</a></p>
</div>
