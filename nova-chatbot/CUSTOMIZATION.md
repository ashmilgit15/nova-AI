# 🎨 Customization Guide - Make Nova Your Own!

This guide shows you how to customize Nova to fit your needs.

---

## 🎭 Changing Nova's Personality

### 1. Edit the System Prompt

The system prompt defines Nova's personality. Find it in `app.py`:

```python
SYSTEM_PROMPT = """You are Nova, a friendly, chill, and conversational coding assistant..."""
```

**Example - Make Nova More Professional:**

```python
SYSTEM_PROMPT = """You are Nova, a professional coding assistant with deep expertise in software development. 

Your traits:
- Professional and articulate
- Focus on best practices and industry standards
- Provide detailed, well-structured responses
- Reference official documentation when relevant
- Ask clarifying questions to understand requirements fully

Your expertise includes Python, software architecture, testing, and deployment."""
```

**Example - Make Nova Beginner-Focused:**

```python
SYSTEM_PROMPT = """You are Nova, a patient and encouraging coding teacher for beginners.

Your traits:
- Break down complex concepts into simple terms
- Use analogies and real-world examples
- Encourage learning and experimentation
- Never assume prior knowledge
- Celebrate small wins and progress

You specialize in teaching Python fundamentals to complete beginners."""
```

### 2. Change the Welcome Message

Find this in the `initialize_session_state()` function:

```python
welcome_message = {
    "role": "assistant",
    "content": "Hey! I'm Nova 😎🐍 — your friendly coding assistant..."
}
```

Customize it to match your use case!

---

## 🎨 Customizing the UI

### 1. Change Colors

Edit the custom CSS in `app.py`:

```python
st.markdown("""
<style>
    .main-header {
        color: #FF6B6B;  /* Change this for header color */
    }
    .sub-header {
        color: #4ECDC4;  /* Change this for subheader color */
    }
    .user-message {
        background-color: #E8F5E9;  /* User message background */
        border-left: 4px solid #4CAF50;  /* User message border */
    }
    .assistant-message {
        background-color: #E3F2FD;  /* Nova message background */
        border-left: 4px solid #2196F3;  /* Nova message border */
    }
</style>
""", unsafe_allow_html=True)
```

**Example - Dark Theme:**

```python
.user-message {
    background-color: #1E1E1E;
    border-left: 4px solid #00FF00;
    color: #FFFFFF;
}
.assistant-message {
    background-color: #2D2D2D;
    border-left: 4px solid #00BFFF;
    color: #FFFFFF;
}
```

### 2. Change the Page Title and Icon

Edit the page config:

```python
st.set_page_config(
    page_title="Nova - Your Coding Buddy",  # Change this
    page_icon="🐍",  # Change this emoji
    layout="wide",
    initial_sidebar_state="expanded"
)
```

**Examples:**
- `page_icon="🤖"` - Robot icon
- `page_icon="💻"` - Laptop icon
- `page_icon="🚀"` - Rocket icon

### 3. Modify the Header

Find and edit:

```python
st.markdown('<div class="main-header">🐍 Nova - Your Coding Buddy</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-header">Friendly AI Assistant for Python & More</div>', unsafe_allow_html=True)
```

---

## 🤖 Changing the AI Model

### Available Groq Models

Find this in the `get_nova_response()` function:

```python
response = st.session_state.groq_client.chat.completions.create(
    model="llama-3.1-70b-versatile",  # Change this
    ...
)
```

**Available models:**

| Model | Speed | Quality | Best For |
|-------|-------|---------|----------|
| `llama-3.1-8b-instant` | ⚡⚡⚡ Very Fast | Good | Quick responses |
| `llama-3.1-70b-versatile` | ⚡⚡ Fast | Excellent | Balanced use |
| `mixtral-8x7b-32768` | ⚡ Moderate | Excellent | Long contexts |
| `gemma2-9b-it` | ⚡⚡ Fast | Good | Instruction following |

### Adjusting Response Creativity

Modify these parameters:

```python
response = st.session_state.groq_client.chat.completions.create(
    model="llama-3.1-70b-versatile",
    messages=messages,
    temperature=0.7,     # 0.0 = deterministic, 1.0 = creative
    max_tokens=2048,     # Maximum response length
    top_p=0.9,          # Nucleus sampling (0.1 to 1.0)
)
```

**Examples:**

**More Creative:**
```python
temperature=0.9
top_p=0.95
```

**More Deterministic:**
```python
temperature=0.3
top_p=0.85
```

**Longer Responses:**
```python
max_tokens=4096
```

---

## 💬 Customizing Conversation History

### Change History Limit

Find this in `get_nova_response()`:

```python
# Add conversation history (limit to last 10 exchanges)
conversation_history = st.session_state.messages[-20:]  # Last 10 exchanges
```

**Examples:**

**More context (uses more tokens):**
```python
conversation_history = st.session_state.messages[-40:]  # Last 20 exchanges
```

**Less context (saves tokens):**
```python
conversation_history = st.session_state.messages[-10:]  # Last 5 exchanges
```

### Add Conversation Export

Add this button in the sidebar:

```python
if st.button("💾 Export Chat"):
    chat_text = "\n\n".join([
        f"{'User' if msg['role'] == 'user' else 'Nova'}: {msg['content']}"
        for msg in st.session_state.messages
    ])
    st.download_button(
        label="Download Chat History",
        data=chat_text,
        file_name="nova_chat_history.txt",
        mime="text/plain"
    )
```

---

## 🎯 Adding New Features

### 1. Code Syntax Highlighting

Install pygments:
```bash
pip install pygments
```

Update requirements.txt:
```
streamlit==1.32.0
groq==0.4.2
python-dotenv==1.0.1
pygments==2.17.2
```

Use `st.code()` for code blocks in responses.

### 2. Message Timestamps

Add timestamps to messages:

```python
# When adding a message
import datetime

st.session_state.messages.append({
    "role": "user",
    "content": user_input,
    "timestamp": datetime.datetime.now().strftime("%H:%M")
})

# When displaying
st.caption(f"🕒 {message.get('timestamp', '')}")
```

### 3. User Feedback Buttons

Add thumbs up/down after each response:

```python
col1, col2 = st.columns([0.05, 0.95])
with col1:
    st.button("👍", key=f"like_{idx}")
    st.button("👎", key=f"dislike_{idx}")
with col2:
    st.markdown(content)
```

### 4. Code Execution Sandbox

**⚠️ Security Warning:** Only run in controlled environments!

```python
import subprocess
import tempfile

def execute_python_code(code):
    """Execute Python code safely"""
    try:
        with tempfile.NamedTemporaryFile(mode='w', suffix='.py', delete=False) as f:
            f.write(code)
            temp_file = f.name
        
        result = subprocess.run(
            ['python', temp_file],
            capture_output=True,
            text=True,
            timeout=5
        )
        return result.stdout
    except Exception as e:
        return f"Error: {str(e)}"
```

### 5. Voice Input (Experimental)

Add speech recognition:

```bash
pip install SpeechRecognition
```

```python
import speech_recognition as sr

if st.button("🎤 Voice Input"):
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)
        text = r.recognize_google(audio)
        st.session_state.voice_input = text
```

---

## 📊 Adding Analytics

### Track Usage Stats

```python
# In initialize_session_state()
if "stats" not in st.session_state:
    st.session_state.stats = {
        "messages_sent": 0,
        "session_start": datetime.datetime.now(),
        "topics": []
    }

# Increment on user message
st.session_state.stats["messages_sent"] += 1

# Display in sidebar
st.sidebar.metric("Messages Sent", st.session_state.stats["messages_sent"])
st.sidebar.metric("Session Duration", 
    str(datetime.datetime.now() - st.session_state.stats["session_start"]).split('.')[0]
)
```

---

## 🎨 Sample Prompt Library

Add a prompt library in the sidebar:

```python
st.sidebar.header("💡 Quick Prompts")

prompts = {
    "Debug Code": "I have a bug in my code. Can you help me debug it?",
    "Write Function": "Write a Python function that...",
    "Explain Concept": "Explain this concept in simple terms:",
    "Optimize Code": "How can I optimize this code?",
    "Best Practices": "What are the best practices for..."
}

selected_prompt = st.sidebar.selectbox("Choose a template:", list(prompts.keys()))
if st.sidebar.button("Use Template"):
    st.session_state.prompt_template = prompts[selected_prompt]
```

---

## 🔧 Advanced Customizations

### 1. Multi-Page Application

Convert to multi-page app structure:

```
nova-chatbot/
├── app.py (main page)
├── pages/
│   ├── 1_Chat.py
│   ├── 2_Settings.py
│   └── 3_History.py
```

### 2. User Profiles

Add persistent user profiles:

```python
import json

def save_profile(username, preferences):
    with open(f"profiles/{username}.json", "w") as f:
        json.dump(preferences, f)

def load_profile(username):
    with open(f"profiles/{username}.json", "r") as f:
        return json.load(f)
```

### 3. Custom API Backend

Replace Groq with your own API:

```python
import requests

def get_custom_api_response(message):
    response = requests.post(
        "https://your-api.com/chat",
        json={"message": message},
        headers={"Authorization": f"Bearer {your_api_key}"}
    )
    return response.json()["response"]
```

---

## 🎨 UI Component Examples

### Add a Sidebar Avatar

```python
st.sidebar.image("nova_avatar.png", width=100)
```

### Add Progress Bars

```python
with st.spinner("Nova is thinking..."):
    progress_bar = st.progress(0)
    for i in range(100):
        time.sleep(0.01)
        progress_bar.progress(i + 1)
```

### Add Expandable Sections

```python
with st.expander("🔧 Advanced Settings"):
    temperature = st.slider("Temperature", 0.0, 1.0, 0.7)
    max_tokens = st.slider("Max Tokens", 512, 4096, 2048)
```

---

## 🚀 Performance Optimizations

### 1. Cache API Responses

```python
@st.cache_data(ttl=3600)
def get_cached_response(message):
    return get_nova_response(message)
```

### 2. Lazy Load Components

```python
@st.cache_resource
def load_model():
    return initialize_groq()
```

### 3. Optimize Session State

```python
# Clear old messages
if len(st.session_state.messages) > 100:
    st.session_state.messages = st.session_state.messages[-50:]
```

---

## 📚 Additional Resources

- **Streamlit Documentation:** [docs.streamlit.io](https://docs.streamlit.io)
- **Groq API Docs:** [console.groq.com/docs](https://console.groq.com/docs)
- **Streamlit Components:** [streamlit.io/components](https://streamlit.io/components)
- **CSS Color Picker:** [htmlcolorcodes.com](https://htmlcolorcodes.com)

---

## 💡 Need Inspiration?

Check out these customization ideas:

- 🎓 **Study Buddy Mode:** Focus on educational explanations
- 🏢 **Enterprise Mode:** Professional tone with documentation
- 🎮 **Game Dev Assistant:** Specialized for game programming
- 📊 **Data Science Mode:** Focus on pandas, numpy, ML
- 🌐 **Web Dev Mode:** HTML, CSS, JavaScript assistance
- 🤖 **AI Research Mode:** Focus on ML models and theory

---

**Happy Customizing! 🎨**

Remember: After making changes, restart your Streamlit app to see them in action!
