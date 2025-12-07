# Culinaryfox-AI
Discover Delicious Recipes Instantly Using What You Have

🔗 Live App: https://culinaryfox-ai.onrender.com
📌 Overview

CulinaryFox AI is an intelligent recipe generator designed to help anyone — especially students and home cooks — transform available ingredients into delicious, beginner-friendly meals.

Just enter the ingredients you have — and the AI returns:

Suggested dishes tailored to your input

Step-by-step instructions

Required & optional ingredients

Time to cook each dish

Say goodbye to food waste, and hello to smart, stress-free cooking. 🍳✨

🚀 Features
Feature	Details
🧠 AI-Generated Recipes	Powered by Llama 3.3-70B (via Groq API)
👨‍🍳 Beginner-friendly	Clear cooking steps with helpful tips
📱 Mobile-responsive UI	Works smoothly on phones, tablets, desktops
⏱ Time estimates	Know how long each dish will take
➕ Optional ingredients	Enhance the recipe if extra items are available
🔐 Secure deployment	API key stored in environment variables
🌍 Live online	Deployed using Render Web Services
🧠 Tech Stack
Layer	Technologies
Frontend	HTML5, CSS3, JavaScript
Backend	Python, Flask
AI Integration	Groq API — Llama 3.3 70B model
Deployment	Render
Version Control	Git & GitHub
🛠 Local Development Setup

Clone the repository:

git clone https://github.com/Alancodess/Culinaryfox-AI.git
cd Culinaryfox-AI


Install dependencies:

pip install -r requirements.txt


Set your Groq API Key:

# Windows (PowerShell)
setx GROQ_API_KEY "your_key_here"

# macOS/Linux
export GROQ_API_KEY="your_key_here"


Run development server:

python app.py


Local app runs at:
👉 http://127.0.0.1:5000

📦 Project Structure
Culinaryfox-AI/
│
├── app.py              # Flask backend + API integration
├── requirements.txt    # Project dependencies
└── templates/
    └── index.html      # User interface

🔐 Environment Variables
Key	Usage
GROQ_API_KEY	Authenticates AI requests

➡️ Must be stored securely (never commit into code)

🚀 Deployment

This project is deployed on Render Web Services with:

Gunicorn as WSGI server

Auto-deploy via GitHub integration

Free tier supported

Optional uptime monitoring via UptimeRobot

📌 Future Enhancements
Priority	Enhancement
⭐⭐⭐⭐⭐	Ingredient selection pills by category
⭐⭐⭐⭐	Voice input (speech to text)
⭐⭐⭐	Dark mode toggle
⭐⭐	AI-generated dish images
⭐	“Recipe of the Day” auto refresh
👤 Author

Built with passion by Alan (“Alancodess”)
👨‍💻 Aspiring AI/ML Engineer
📌 India

If you like this project, please ⭐ the repository — it helps a lot!
