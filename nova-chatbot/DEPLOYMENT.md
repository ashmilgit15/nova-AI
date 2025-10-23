# 🌐 Deployment Guide - Host Nova Online for Free!

This guide shows you how to deploy Nova to three popular free hosting platforms.

---

## 🎯 Option 1: Streamlit Community Cloud (Recommended)

**Best for:** Easiest deployment, perfect for Streamlit apps
**Cost:** 100% Free
**Deploy time:** ~5 minutes

### Step-by-Step Instructions:

#### 1. Prepare Your Code

Make sure all files are committed to GitHub:

```bash
# Initialize git (if not already done)
git init

# Add all files
git add .

# Commit
git commit -m "Initial commit - Nova AI chatbot"

# Create main branch
git branch -M main
```

#### 2. Push to GitHub

```bash
# Create a new repository on GitHub first, then:
git remote add origin https://github.com/YOUR_USERNAME/nova-chatbot.git
git push -u origin main
```

#### 3. Deploy on Streamlit Cloud

1. Go to **[share.streamlit.io](https://share.streamlit.io)**
2. Click **"Sign in with GitHub"**
3. Click **"New app"**
4. Select:
   - Repository: `YOUR_USERNAME/nova-chatbot`
   - Branch: `main`
   - Main file path: `app.py`
5. Click **"Advanced settings"**
6. In the **Secrets** section, add:
   ```toml
   GROQ_API_KEY = "your_actual_groq_api_key_here"
   ```
7. Click **"Deploy"**!

#### 4. Share Your App

Your app will be live at:
```
https://YOUR_USERNAME-nova-chatbot.streamlit.app
```

### Managing Your Deployment

- **Update code:** Just push to GitHub, Streamlit auto-deploys
- **View logs:** Click "Manage app" → "Logs"
- **Update secrets:** "Manage app" → "Settings" → "Secrets"
- **Custom domain:** Available on paid plans

---

## 🤗 Option 2: Hugging Face Spaces

**Best for:** ML community exposure, easy sharing
**Cost:** 100% Free (with CPU/GPU options)
**Deploy time:** ~10 minutes

### Step-by-Step Instructions:

#### 1. Create a Hugging Face Account

- Go to **[huggingface.co](https://huggingface.co)** and sign up

#### 2. Create a New Space

1. Click your profile → **"Spaces"** → **"Create new Space"**
2. Fill in:
   - **Space name:** `nova-chatbot` (or any name you like)
   - **License:** MIT (or your choice)
   - **Select the SDK:** **Streamlit**
   - **Space hardware:** CPU (free tier)
3. Click **"Create Space"**

#### 3. Upload Files

**Option A - Web Upload:**
1. Click "Files" tab
2. Click "Add file" → "Upload files"
3. Upload: `app.py`, `requirements.txt`, `README.md`
4. Commit changes

**Option B - Git Push:**
```bash
# Clone your Space
git clone https://huggingface.co/spaces/YOUR_USERNAME/nova-chatbot
cd nova-chatbot

# Copy your files
cp /path/to/nova-chatbot/* .

# Push to HF
git add .
git commit -m "Initial deployment"
git push
```

#### 4. Configure Secrets

1. Go to your Space → **Settings**
2. Scroll to **"Repository secrets"**
3. Click **"Add a new secret"**
4. Add:
   - **Name:** `GROQ_API_KEY`
   - **Value:** `your_actual_groq_api_key_here`
5. Click **"Add secret"**

#### 5. Access Your App

Your Space will be live at:
```
https://huggingface.co/spaces/YOUR_USERNAME/nova-chatbot
```

### Benefits of Hugging Face Spaces

- ✅ Easy sharing in ML community
- ✅ Can upgrade to GPU for free
- ✅ Built-in version control
- ✅ Community discussions on your Space
- ✅ Can duplicate and remix others' Spaces

---

## 🔄 Option 3: Replit

**Best for:** Quick prototyping, browser-based development
**Cost:** Free tier available
**Deploy time:** ~5 minutes

### Step-by-Step Instructions:

#### 1. Create a Replit Account

- Go to **[replit.com](https://replit.com)** and sign up

#### 2. Create a New Repl

**Option A - Import from GitHub:**
1. Click **"+ Create Repl"**
2. Select **"Import from GitHub"**
3. Enter your GitHub repo URL
4. Click **"Import from GitHub"**

**Option B - Manual Setup:**
1. Click **"+ Create Repl"**
2. Select **"Python"** template
3. Name it: `nova-chatbot`
4. Upload your files via drag-and-drop

#### 3. Configure Environment

1. Click the **"Secrets"** icon (🔒) in the left sidebar
2. Add a new secret:
   - **Key:** `GROQ_API_KEY`
   - **Value:** `your_actual_groq_api_key_here`

#### 4. Configure Run Settings

Create a `.replit` file in the root:

```toml
run = "streamlit run app.py --server.port 8080 --server.address 0.0.0.0"
language = "python3"

[env]
PYTHONUNBUFFERED = "1"
```

#### 5. Run Your App

1. Click the **"Run"** button
2. Replit will:
   - Install dependencies from `requirements.txt`
   - Start your Streamlit app
   - Show you the live URL

#### 6. Share Your Repl

Your app will be accessible at:
```
https://nova-chatbot.YOUR_USERNAME.repl.co
```

### Replit Features

- ✅ Browser-based IDE (no local setup needed)
- ✅ Real-time collaboration
- ✅ Always-on deployments (on paid plans)
- ✅ Built-in version control
- ✅ Easy to fork and experiment

---

## 🔒 Security Best Practices

### DO:
- ✅ Always use secrets/environment variables for API keys
- ✅ Add `.env` to `.gitignore`
- ✅ Use different API keys for dev and production
- ✅ Regularly rotate your API keys

### DON'T:
- ❌ Never commit `.env` files to Git
- ❌ Never hardcode API keys in your code
- ❌ Never share your API keys publicly
- ❌ Never commit secrets in code comments

---

## 📊 Comparison Table

| Feature | Streamlit Cloud | Hugging Face | Replit |
|---------|----------------|--------------|--------|
| **Ease of Setup** | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ |
| **Free Tier** | Unlimited | Unlimited | Limited hours |
| **Custom Domain** | Paid only | No | Paid only |
| **Best For** | Streamlit apps | ML projects | Quick prototypes |
| **Community** | Streamlit users | ML community | Developers |
| **Deployment Speed** | Auto-deploy | Auto-deploy | Manual run |

---

## 🚀 Post-Deployment Checklist

After deploying, test these:

- [ ] App loads without errors
- [ ] API key is working (test with a query)
- [ ] Chat history persists during session
- [ ] All UI elements display correctly
- [ ] Mobile responsiveness works
- [ ] Share link works for others
- [ ] Error messages display properly

---

## 🔧 Troubleshooting Deployment

### Issue: "Module not found" error

**Solution:**
- Check `requirements.txt` includes all dependencies
- Verify correct versions
- Try clearing build cache and redeploying

### Issue: "API key not found" error

**Solution:**
- Verify secret is named exactly `GROQ_API_KEY`
- Check for extra spaces in secret value
- Restart the app after adding secrets

### Issue: App runs locally but not after deployment

**Solution:**
- Check platform-specific logs
- Verify all file paths are correct
- Ensure no local-only dependencies
- Check Python version compatibility

### Issue: Slow response times

**Solution:**
- Check your Groq API rate limits
- Consider upgrading to paid hosting for more resources
- Optimize model selection (use `llama-3.1-8b-instant` for faster responses)

---

## 📈 Monitoring Your Deployment

### Streamlit Cloud:
- View logs: App menu → "Manage app" → "Logs"
- Check analytics: App menu → "Manage app" → "Analytics"

### Hugging Face:
- View logs: Space page → "Logs" tab
- Check discussions: Space page → "Community" tab

### Replit:
- View console: Console tab while app is running
- Check resource usage: Available in sidebar

---

## 🎉 You're Done!

Your Nova chatbot is now live and accessible to anyone with the link!

**Next Steps:**
- Share your deployment with friends
- Customize Nova's personality in `app.py`
- Add new features (see README for ideas)
- Monitor usage and gather feedback

**Need help?** Check the main README.md or open an issue on GitHub!
