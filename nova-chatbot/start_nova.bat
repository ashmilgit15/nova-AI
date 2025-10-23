@echo off
echo.
echo ===============================================
echo    Starting Nova - Your AI Coding Assistant
echo ===============================================
echo.

REM Check if .env file exists
if not exist ".env" (
    echo [WARNING] .env file not found!
    echo.
    echo Creating .env from template...
    copy .env.example .env
    echo.
    echo Please edit .env file and add your GROQ_API_KEY
    echo Get your key from: https://console.groq.com/keys
    echo.
    echo After adding your API key, run this script again.
    echo.
    pause
    exit /b
)

echo [1/3] Checking Python installation...
python --version >nul 2>&1
if errorlevel 1 (
    echo [ERROR] Python not found! Please install Python 3.8+
    echo Download from: https://www.python.org/downloads/
    pause
    exit /b
)
echo [OK] Python found!
echo.

echo [2/3] Installing dependencies...
pip install -r requirements.txt --quiet
if errorlevel 1 (
    echo [ERROR] Failed to install dependencies
    pause
    exit /b
)
echo [OK] Dependencies installed!
echo.

echo [3/3] Starting Nova...
echo.
echo ===============================================
echo   Nova will open in your browser shortly...
echo   Press Ctrl+C to stop the server
echo ===============================================
echo.

streamlit run app.py

pause
