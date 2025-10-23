"""
Test script to verify Nova setup is correct
Run this before starting the main app to check everything is configured properly
"""

import sys
import os
from dotenv import load_dotenv

def test_python_version():
    """Check if Python version is 3.8 or higher"""
    print("🐍 Checking Python version...")
    version = sys.version_info
    if version.major >= 3 and version.minor >= 8:
        print(f"   ✅ Python {version.major}.{version.minor}.{version.micro} - Good to go!")
        return True
    else:
        print(f"   ❌ Python {version.major}.{version.minor}.{version.micro} - Need 3.8 or higher")
        return False

def test_dependencies():
    """Check if required packages are installed"""
    print("\n📦 Checking dependencies...")
    required_packages = ["streamlit", "groq", "dotenv"]
    all_installed = True
    
    for package in required_packages:
        try:
            if package == "dotenv":
                __import__("dotenv")
            else:
                __import__(package)
            print(f"   ✅ {package} - Installed")
        except ImportError:
            print(f"   ❌ {package} - Not installed")
            all_installed = False
    
    if not all_installed:
        print("\n   💡 Install missing packages with: pip install -r requirements.txt")
    
    return all_installed

def test_api_key():
    """Check if GROQ API key is configured"""
    print("\n🔑 Checking API key configuration...")
    load_dotenv()
    
    api_key = os.getenv("GROQ_API_KEY")
    
    if api_key and api_key != "your_groq_api_key_here":
        # Mask the key for security
        masked_key = api_key[:8] + "..." + api_key[-4:] if len(api_key) > 12 else "***"
        print(f"   ✅ API key found: {masked_key}")
        return True
    else:
        print("   ❌ API key not configured or still using placeholder")
        print("\n   💡 Steps to fix:")
        print("      1. Copy .env.example to .env")
        print("      2. Get your API key from: https://console.groq.com/keys")
        print("      3. Add it to the .env file")
        return False

def test_groq_connection():
    """Test connection to Groq API"""
    print("\n🌐 Testing Groq API connection...")
    
    load_dotenv()
    api_key = os.getenv("GROQ_API_KEY")
    
    if not api_key or api_key == "your_groq_api_key_here":
        print("   ⏭️  Skipping (API key not configured)")
        return False
    
    try:
        from groq import Groq
        client = Groq(api_key=api_key)
        
        # Try a simple test request
        response = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[{"role": "user", "content": "Say 'Hello!' in one word"}],
            max_tokens=10
        )
        
        if response.choices[0].message.content:
            print("   ✅ API connection successful!")
            print(f"   🤖 Test response: {response.choices[0].message.content.strip()}")
            return True
        else:
            print("   ❌ API responded but with empty content")
            return False
            
    except Exception as e:
        print(f"   ❌ Connection failed: {str(e)}")
        print("\n   💡 Common issues:")
        print("      - Invalid API key")
        print("      - No internet connection")
        print("      - API rate limit reached")
        return False

def main():
    """Run all tests"""
    print("=" * 60)
    print("🚀 Nova Setup Verification")
    print("=" * 60)
    
    results = {
        "Python Version": test_python_version(),
        "Dependencies": test_dependencies(),
        "API Key": test_api_key(),
    }
    
    # Only test connection if API key is configured
    if results["API Key"]:
        results["API Connection"] = test_groq_connection()
    
    print("\n" + "=" * 60)
    print("📊 Test Summary")
    print("=" * 60)
    
    for test, result in results.items():
        status = "✅ PASS" if result else "❌ FAIL"
        print(f"{test:20} {status}")
    
    all_passed = all(results.values())
    
    print("\n" + "=" * 60)
    if all_passed:
        print("🎉 All tests passed! You're ready to run Nova!")
        print("\nRun this command to start Nova:")
        print("   streamlit run app.py")
    else:
        print("⚠️  Some tests failed. Please fix the issues above.")
        print("\nCheck QUICKSTART.md for detailed setup instructions.")
    print("=" * 60)

if __name__ == "__main__":
    main()
