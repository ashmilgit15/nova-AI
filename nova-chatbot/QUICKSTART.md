# 🚀 Quick Start Guide - Get Nova Running in 5 Minutes!

Follow these simple steps to get Nova up and running:

## Step 1: Get Your Free Groq API Key ⚡

1. Visit **[console.groq.com](https://console.groq.com)**
2. Sign up (it's free!)
3. Go to "API Keys" section
4. Click "Create API Key"
5. **Copy the key** (you'll need it in the next step)

## Step 2: Set Up Your Environment 🔧

### Windows:
```powershell
# Navigate to the nova-chatbot folder
cd "C:\Users\Ashmil P\Desktop\AI Projects\nova-chatbot"

# Install dependencies
pip install -r requirements.txt

# Create .env file
copy .env.example .env

# Open .env in notepad and paste your API key
notepad .env
```

### Mac/Linux:
```bash
# Navigate to the nova-chatbot folder
cd nova-chatbot

# Install dependencies
pip install -r requirements.txt

# Create .env file
cp .env.example .env

# Open .env and paste your API key
nano .env
```

**In the .env file, replace `your_groq_api_key_here` with your actual API key:**
```
GROQ_API_KEY=gsk_your_actual_key_here
```

## Step 3: Run Nova! 🐍

```bash
streamlit run app.py
```

That's it! Nova will open in your browser at `http://localhost:8501` 🎉

## First Time Using Nova?

Try these conversation starters:

1. "Hey Nova! Can you explain what Python decorators are?"
2. "I need help writing a function to sort a list of dictionaries."
3. "Let's brainstorm an AI project idea for beginners."
4. "Can you help me debug this code?" (paste your code)
5. "Give me tips on writing better prompts for AI models."

---

## Troubleshooting 🔧

### Problem: "GROQ_API_KEY not found"
- **Solution**: Make sure your `.env` file exists and contains your API key
- Check that the file is named exactly `.env` (not `.env.txt`)
- Restart the Streamlit app after creating the `.env` file

### Problem: "Module not found"
- **Solution**: Run `pip install -r requirements.txt` again
- Make sure you're in the correct directory

### Problem: Port already in use
- **Solution**: Streamlit will automatically choose another port (like 8502, 8503)
- Or stop other Streamlit apps: `Ctrl+C` in the terminal

---

## Need More Help?

- 📖 Read the full **[README.md](README.md)** for detailed instructions
- 💬 Check [Groq Documentation](https://console.groq.com/docs)
- 🐛 Check [Streamlit Documentation](https://docs.streamlit.io)

**Enjoy chatting with Nova!** 😎🐍
