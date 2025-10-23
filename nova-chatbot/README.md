# 🐍 Nova - Your Friendly AI Coding Assistant

<div align="center">

![Nova Banner](https://img.shields.io/badge/Nova-AI%20Coding%20Assistant-FF6B6B?style=for-the-badge)
![Python](https://img.shields.io/badge/Python-3.8+-blue?style=for-the-badge&logo=python)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![Groq](https://img.shields.io/badge/Groq-API-orange?style=for-the-badge)

**A chill, conversational AI chatbot for Python programming, debugging, and AI project ideas** 😎

</div>

---

## 🌟 Features

- **🤖 Friendly AI Assistant**: Nova is like having a coding buddy who's always ready to help
- **💬 Natural Conversations**: Chat naturally with context-aware responses
- **🧠 Session Memory**: Nova remembers your conversation during the current session
- **🎨 Clean UI**: Beautiful, modern interface built with Streamlit
- **⚡ Fast Responses**: Powered by Groq's ultra-fast inference API
- **🐍 Python Expert**: Specialized in Python programming, debugging, and optimization
- **💡 Project Ideation**: Brainstorm AI project ideas together
- **📝 Prompt Engineering**: Get advice on crafting better prompts

---

## 📋 What Nova Can Help With

- ✅ Python programming (all skill levels)
- ✅ Debugging and optimizing code
- ✅ Prompt engineering advice
- ✅ Brainstorming AI project ideas
- ✅ Explaining complex concepts in simple terms
- ✅ General coding tasks and best practices

---

## 🚀 Quick Start Guide

### Prerequisites

- Python 3.8 or higher
- A free Groq API key ([Get one here](https://console.groq.com/keys))

### Installation

1. **Clone or download this repository**
   ```bash
   cd nova-chatbot
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up your API key**
   
   **Option A: Using Environment Variables (Recommended for local development)**
   
   Create a `.env` file in the project root:
   ```bash
   # Copy the example file
   copy .env.example .env
   ```
   
   Edit `.env` and add your Groq API key:
   ```
   GROQ_API_KEY=your_actual_groq_api_key_here
   ```

   **Option B: Using Streamlit Secrets (Recommended for deployment)**
   
   Create `.streamlit/secrets.toml`:
   ```toml
   GROQ_API_KEY = "your_actual_groq_api_key_here"
   ```

4. **Run Nova!**
   ```bash
   streamlit run app.py
   ```

5. **Open your browser**
   - Nova will automatically open at `http://localhost:8501`
   - Start chatting! 🎉

---

## 🎯 Sample Conversation Starters

Try these prompts to get started with Nova:

- 🐍 "Can you write a Python script to process data?"
- 🐛 "I need help debugging this function."
- 💬 "Give me advice on prompt engineering for my AI model."
- 💡 "Let's brainstorm an AI project idea."
- 📚 "Explain this Python concept in simple terms."

---

## 🌐 Free Deployment Options

### Option 1: Streamlit Community Cloud (Recommended - Easiest)

**100% Free hosting for Streamlit apps!**

1. **Push your code to GitHub**
   ```bash
   git init
   git add .
   git commit -m "Initial commit - Nova chatbot"
   git branch -M main
   git remote add origin YOUR_GITHUB_REPO_URL
   git push -u origin main
   ```

2. **Deploy on Streamlit Cloud**
   - Go to [share.streamlit.io](https://share.streamlit.io)
   - Sign in with GitHub
   - Click "New app"
   - Select your repository and `app.py`
   - Add your `GROQ_API_KEY` in the "Secrets" section:
     ```toml
     GROQ_API_KEY = "your_actual_groq_api_key_here"
     ```
   - Click "Deploy"!

3. **Share your app**
   - Your app will be live at `https://your-app-name.streamlit.app`
   - Share the link with anyone! 🎉

### Option 2: Hugging Face Spaces

**Free GPU/CPU hosting with great ML community support!**

1. **Create a new Space**
   - Go to [huggingface.co/spaces](https://huggingface.co/spaces)
   - Click "Create new Space"
   - Select "Streamlit" as the SDK
   - Name it (e.g., "nova-chatbot")

2. **Upload your files**
   - Upload `app.py` and `requirements.txt`
   - Go to Settings → Variables and Secrets
   - Add `GROQ_API_KEY` as a secret

3. **Your app is live!**
   - Access at `https://huggingface.co/spaces/YOUR_USERNAME/nova-chatbot`

### Option 3: Replit

**Browser-based IDE with instant deployment!**

1. **Create a new Repl**
   - Go to [replit.com](https://replit.com)
   - Click "+ Create Repl"
   - Choose "Import from GitHub" or upload files manually

2. **Configure environment**
   - Click on "Secrets" (lock icon)
   - Add `GROQ_API_KEY` as a secret

3. **Run the app**
   - Replit will auto-install dependencies
   - Click "Run" button
   - Your app will be live!

---

## 🛠️ Project Structure

```
nova-chatbot/
│
├── app.py                 # Main Streamlit application
├── requirements.txt       # Python dependencies
├── .env.example          # Environment variables template
├── .gitignore            # Git ignore file
└── README.md             # This file!
```

---

## ⚙️ Configuration

### Customizing Nova's Personality

Edit the `SYSTEM_PROMPT` in `app.py` to customize Nova's personality, tone, or expertise areas:

```python
SYSTEM_PROMPT = """You are Nova, a friendly, chill, and conversational coding assistant..."""
```

### Changing the AI Model

Nova uses Groq's `llama-3.1-70b-versatile` model by default. You can change it in `app.py`:

```python
response = st.session_state.groq_client.chat.completions.create(
    model="llama-3.1-70b-versatile",  # Change this to another Groq model
    ...
)
```

Available Groq models:
- `llama-3.1-70b-versatile` (Default - Fast and capable)
- `llama-3.1-8b-instant` (Faster, lighter)
- `mixtral-8x7b-32768` (Great for longer contexts)

### Adjusting Response Style

Modify these parameters in the API call:

```python
temperature=0.7,      # 0.0 = deterministic, 1.0 = creative
max_tokens=2048,      # Maximum response length
top_p=0.9,           # Nucleus sampling
```

---

## 🔑 Getting Your Free Groq API Key

1. Visit [console.groq.com](https://console.groq.com)
2. Sign up for a free account
3. Navigate to "API Keys" section
4. Click "Create API Key"
5. Copy your key and add it to `.env` or Streamlit secrets

**Free Tier Includes:**
- ✅ 30 requests per minute
- ✅ 15,000 tokens per minute
- ✅ No credit card required!

---

## 💡 Tips for Using Nova

1. **Be Specific**: The more details you provide, the better Nova can help
2. **Share Code**: Paste code snippets directly in the chat for debugging
3. **Ask Follow-ups**: Nova remembers the conversation, so build on previous topics
4. **Clear Chat**: Use the sidebar button to start fresh conversations
5. **Explore Prompts**: Try the sample prompts in the sidebar

---

## 🐛 Troubleshooting

### "GROQ_API_KEY not found" Error

**Solution**: Make sure you've set up your API key correctly:
- For local: Create `.env` file with your key
- For deployment: Add key to Streamlit secrets or Hugging Face secrets

### "API Rate Limit" Error

**Solution**: 
- Wait a few seconds between requests
- Groq's free tier allows 30 requests/minute
- Consider upgrading if you need more

### App Not Loading

**Solution**:
- Check that all dependencies are installed: `pip install -r requirements.txt`
- Verify Python version: `python --version` (should be 3.8+)
- Try clearing cache: `streamlit cache clear`

---

## 🎨 Customization Ideas

- **Add Voice Input**: Integrate speech-to-text for voice queries
- **Code Execution**: Add a sandbox environment to run Python code
- **Save Conversations**: Implement export to PDF or text file
- **Multi-language**: Extend Nova to support multiple programming languages
- **Theme Toggle**: Add dark/light mode switcher
- **User Profiles**: Implement persistent user preferences

---

## 📝 Code Quality

- ✅ **Clean & Modular**: Well-organized, readable code
- ✅ **Well-Commented**: Extensive comments explaining functionality
- ✅ **Beginner-Friendly**: Easy to understand and modify
- ✅ **Error Handling**: Graceful error management
- ✅ **Best Practices**: Follows Python and Streamlit conventions

---

## 🤝 Contributing

Want to make Nova even better? Contributions are welcome!

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

---

## 📄 License

This project is open source and available under the MIT License.

---

## 🙏 Acknowledgments

- **Groq** - For providing ultra-fast AI inference API
- **Streamlit** - For the amazing web framework
- **Meta** - For the Llama models
- **You** - For using Nova! 🎉

---

## 📞 Support

Having issues or questions?

- 📖 Check the [Groq Documentation](https://console.groq.com/docs)
- 💬 Check the [Streamlit Documentation](https://docs.streamlit.io)
- 🐛 Open an issue on GitHub

---

<div align="center">

**Made with ❤️ and Python**

⭐ Star this repo if you find Nova helpful!

</div>
