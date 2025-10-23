#!/bin/bash

echo ""
echo "==============================================="
echo "   Starting Nova - Your AI Coding Assistant"
echo "==============================================="
echo ""

# Check if .env file exists
if [ ! -f ".env" ]; then
    echo "[WARNING] .env file not found!"
    echo ""
    echo "Creating .env from template..."
    cp .env.example .env
    echo ""
    echo "Please edit .env file and add your GROQ_API_KEY"
    echo "Get your key from: https://console.groq.com/keys"
    echo ""
    echo "Run this command to edit:"
    echo "  nano .env"
    echo ""
    echo "After adding your API key, run this script again."
    echo ""
    exit 1
fi

echo "[1/3] Checking Python installation..."
if ! command -v python3 &> /dev/null; then
    echo "[ERROR] Python 3 not found! Please install Python 3.8+"
    echo "Visit: https://www.python.org/downloads/"
    exit 1
fi
echo "[OK] Python found: $(python3 --version)"
echo ""

echo "[2/3] Installing dependencies..."
pip3 install -r requirements.txt --quiet
if [ $? -ne 0 ]; then
    echo "[ERROR] Failed to install dependencies"
    exit 1
fi
echo "[OK] Dependencies installed!"
echo ""

echo "[3/3] Starting Nova..."
echo ""
echo "==============================================="
echo "  Nova will open in your browser shortly..."
echo "  Press Ctrl+C to stop the server"
echo "==============================================="
echo ""

streamlit run app.py
