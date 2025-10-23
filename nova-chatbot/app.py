"""
Nova - A Friendly AI Coding Assistant
A chill, conversational chatbot for Python programming, debugging, and AI project ideas.
"""

import streamlit as st
import os
from groq import Groq
from datetime import datetime
from dotenv import load_dotenv

# Load environment variables from .env file (for local development)
load_dotenv()

# Page configuration
st.set_page_config(
    page_title="Nova - Your Coding Buddy",
    page_icon="🐍",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for better UI
st.markdown("""
<style>
    /* Main Headers */
    .main-header {
        font-size: 2.8rem;
        font-weight: 800;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-align: center;
        margin-bottom: 0.5rem;
        letter-spacing: -0.5px;
    }
    .sub-header {
        font-size: 1.1rem;
        color: #6c757d;
        text-align: center;
        margin-bottom: 2rem;
        font-weight: 400;
    }
    
    /* Chat Container */
    .chat-container {
        max-width: 900px;
        margin: 0 auto;
        padding: 1rem 0;
    }
    
    /* Message Wrapper */
    .message-wrapper {
        display: flex;
        margin-bottom: 1.5rem;
        animation: slideIn 0.3s ease-out;
    }
    
    .message-wrapper.user {
        justify-content: flex-end;
    }
    
    .message-wrapper.assistant {
        justify-content: flex-start;
    }
    
    /* Avatar */
    .avatar {
        width: 40px;
        height: 40px;
        border-radius: 50%;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 1.3rem;
        flex-shrink: 0;
        box-shadow: 0 2px 8px rgba(0,0,0,0.1);
    }
    
    .avatar.user {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        margin-left: 12px;
        order: 2;
    }
    
    .avatar.assistant {
        background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
        margin-right: 12px;
    }
    
    /* Message Bubble */
    .message-bubble {
        max-width: 70%;
        padding: 1rem 1.25rem;
        border-radius: 20px;
        box-shadow: 0 2px 12px rgba(0,0,0,0.08);
        line-height: 1.6;
        position: relative;
    }
    
    .message-bubble.user {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        border-bottom-right-radius: 4px;
    }
    
    .message-bubble.assistant {
        background: #f8f9fa;
        color: #212529;
        border-bottom-left-radius: 4px;
        border: 1px solid #e9ecef;
    }
    
    .message-bubble.welcome {
        max-width: 85%;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        border-radius: 20px;
        padding: 1.5rem;
        box-shadow: 0 4px 20px rgba(102, 126, 234, 0.3);
        border: none;
    }
    
    .message-bubble strong {
        display: block;
        margin-bottom: 0.5rem;
        font-weight: 600;
    }
    
    .message-bubble.user strong {
        color: #ffd700;
    }
    
    .message-bubble.assistant strong {
        color: #764ba2;
    }
    
    .message-bubble.welcome strong {
        color: #ffd700;
        font-size: 1.2rem;
        margin-bottom: 0.75rem;
    }
    
    /* Animations */
    @keyframes slideIn {
        from {
            opacity: 0;
            transform: translateY(15px);
        }
        to {
            opacity: 1;
            transform: translateY(0);
        }
    }
    
    /* Sidebar Styling */
    .stButton>button {
        width: 100%;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        border-radius: 10px;
        padding: 0.6rem;
        font-weight: 600;
        border: none;
        transition: transform 0.2s, box-shadow 0.2s;
    }
    
    .stButton>button:hover {
        transform: translateY(-2px);
        box-shadow: 0 4px 12px rgba(102, 126, 234, 0.4);
    }
    
    /* Input Area */
    .stChatInput {
        border-radius: 25px;
    }
    
    /* Scrollbar Styling */
    ::-webkit-scrollbar {
        width: 8px;
    }
    
    ::-webkit-scrollbar-track {
        background: #f1f1f1;
        border-radius: 10px;
    }
    
    ::-webkit-scrollbar-thumb {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        border-radius: 10px;
    }
    
    ::-webkit-scrollbar-thumb:hover {
        background: #764ba2;
    }
</style>
""", unsafe_allow_html=True)

# Initialize Groq client
def initialize_groq():
    """Initialize the Groq API client"""
    # Try to get API key from Streamlit secrets first (for deployment)
    # Then fall back to environment variables (for local development)
    api_key = None
    
    # Check Streamlit secrets
    try:
        api_key = st.secrets.get("GROQ_API_KEY")
    except (FileNotFoundError, KeyError):
        pass
    
    # Fall back to environment variable
    if not api_key:
        api_key = os.getenv("GROQ_API_KEY")
    
    if not api_key:
        st.error("⚠️ GROQ_API_KEY not found! Please set it in your environment variables or Streamlit secrets.")
        st.info("💡 Get your free API key from: https://console.groq.com/keys")
        st.info("""
        **For local development:**
        1. Copy `.env.example` to `.env`
        2. Add your API key to `.env`
        
        **For Streamlit Cloud:**
        1. Go to your app settings
        2. Add GROQ_API_KEY in the Secrets section
        """)
        st.stop()
    
    return Groq(api_key=api_key)

# Initialize session state
def initialize_session_state():
    """Initialize session state variables for conversation history"""
    if "messages" not in st.session_state:
        st.session_state.messages = []
        # Add welcome message
        welcome_message = {
            "role": "assistant",
            "content": "Hey! I'm Nova 😎🐍 — your friendly coding assistant. I can help you write Python code, debug scripts, brainstorm AI project ideas, and give prompt engineering advice. What coding adventure are we starting today?"
        }
        st.session_state.messages.append(welcome_message)
    
    if "groq_client" not in st.session_state:
        st.session_state.groq_client = initialize_groq()

# System prompt that defines Nova's personality
SYSTEM_PROMPT = """You are Nova, a friendly, chill, and conversational coding assistant. Your personality traits:

- You're approachable and casual, like a coding buddy
- You use a relaxed, upbeat tone with occasional light humor
- You're knowledgeable about Python programming, debugging, optimization, prompt engineering, and AI projects
- You give clear, concise, and helpful responses
- You can use emojis sparingly to enhance your tone (but don't overdo it)
- You explain complex concepts in beginner-friendly terms
- You're encouraging and supportive when users face challenges

Your expertise includes:
- Python programming (all levels)
- Debugging and optimizing code
- Prompt engineering advice
- Brainstorming AI project ideas
- General coding tasks and best practices

Keep responses conversational but informative. Break down complex topics into digestible chunks."""

def get_nova_response(user_message):
    """Get response from Nova using Groq API"""
    try:
        # Prepare messages for API call (include conversation history)
        messages = [{"role": "system", "content": SYSTEM_PROMPT}]
        
        # Add conversation history (limit to last 10 exchanges to manage token usage)
        conversation_history = st.session_state.messages[-20:]  # Last 10 exchanges (user + assistant)
        for msg in conversation_history:
            if msg["role"] != "system":
                messages.append({"role": msg["role"], "content": msg["content"]})
        
        # Add current user message
        messages.append({"role": "user", "content": user_message})
        
        # Make API call to Groq
        response = st.session_state.groq_client.chat.completions.create(
            model="llama-3.3-70b-versatile",  # Latest fast and capable model
            messages=messages,
            temperature=0.7,  # Balanced creativity and coherence
            max_tokens=2048,
            top_p=0.9,
        )
        
        return response.choices[0].message.content
    
    except Exception as e:
        return f"Oops! 😅 I ran into an issue: {str(e)}\n\nMake sure your GROQ_API_KEY is valid and you have API credits available."

def display_chat_history():
    """Display the conversation history with modern chat bubbles"""
    for idx, message in enumerate(st.session_state.messages):
        role = message["role"]
        content = message["content"]
        
        if role == "user":
            # User message - right aligned with avatar
            st.markdown(f'''
                <div class="message-wrapper user">
                    <div class="message-bubble user">
                        {content}
                    </div>
                    <div class="avatar user">👤</div>
                </div>
            ''', unsafe_allow_html=True)
        else:  # assistant
            # First message is the welcome message - give it special styling
            if idx == 0:
                st.markdown(f'''
                    <div class="message-wrapper assistant">
                        <div class="avatar assistant">🤖</div>
                        <div class="message-bubble welcome">
                            <strong>👋 Hey there! I'm Nova</strong>
                            {content}
                        </div>
                    </div>
                ''', unsafe_allow_html=True)
            else:
                # Regular assistant message - left aligned with avatar
                st.markdown(f'''
                    <div class="message-wrapper assistant">
                        <div class="avatar assistant">🤖</div>
                        <div class="message-bubble assistant">
                            {content}
                        </div>
                    </div>
                ''', unsafe_allow_html=True)

def main():
    """Main application logic"""
    # Initialize session state
    initialize_session_state()
    
    # Header
    st.markdown('<div class="main-header">🐍 Nova - Your Coding Buddy</div>', unsafe_allow_html=True)
    st.markdown('<div class="sub-header">Friendly AI Assistant for Python & More</div>', unsafe_allow_html=True)
    
    # Sidebar with sample prompts and info
    with st.sidebar:
        st.header("💡 Sample Prompts")
        st.markdown("""
        Try these conversation starters:
        
        - 🐍 Can you write a Python script to process data?
        - 🐛 I need help debugging this function.
        - 💬 Give me advice on prompt engineering for my AI model.
        - 💡 Let's brainstorm an AI project idea.
        - 📚 Explain this Python concept in simple terms.
        """)
        
        st.divider()
        
        st.header("ℹ️ About Nova")
        st.markdown("""
        Nova is your friendly coding assistant specializing in:
        - Python programming
        - Code debugging & optimization
        - Prompt engineering
        - AI project ideation
        - General coding help
        
        **Session Memory**: Nova remembers our conversation during this session only!
        """)
        
        st.divider()
        
        # Clear chat button
        if st.button("🗑️ Clear Chat History"):
            st.session_state.messages = []
            # Re-add welcome message
            welcome_message = {
                "role": "assistant",
                "content": "Hey! I'm Nova 😎🐍 — your friendly coding assistant. I can help you write Python code, debug scripts, brainstorm AI project ideas, and give prompt engineering advice. What coding adventure are we starting today?"
            }
            st.session_state.messages.append(welcome_message)
            st.rerun()
        
        st.divider()
        
        # Stats
        st.header("📊 Session Stats")
        message_count = len([m for m in st.session_state.messages if m["role"] == "user"])
        st.metric("Messages Sent", message_count)
        st.caption(f"Session started: {datetime.now().strftime('%H:%M')}")
    
    # Main chat area
    chat_container = st.container()
    
    with chat_container:
        # Display chat history
        display_chat_history()
    
    # Chat input at the bottom
    st.divider()
    
    # User input
    user_input = st.chat_input("Type your message here... 💬")
    
    if user_input:
        # Add user message to history
        st.session_state.messages.append({"role": "user", "content": user_input})
        
        # Get Nova's response
        with st.spinner("Nova is thinking... 🤔"):
            nova_response = get_nova_response(user_input)
        
        # Add Nova's response to history
        st.session_state.messages.append({"role": "assistant", "content": nova_response})
        
        # Rerun to update the chat display
        st.rerun()

if __name__ == "__main__":
    main()
