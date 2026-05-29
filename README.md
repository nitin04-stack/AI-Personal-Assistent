# AI Personal Assistant
A simple web app that lets you ask questions and summarize emails using Google Gemini AI. Built with Python and Flask, deployed on Render.

🔗 **Live:** [ai-personal-assistent.onrender.com](https://https://ai-personal-assistent-1yx6.onrender.com/)

## What it does
**Ask Anything** — Type any question and get a clean, straight-to-the-point answer powered by Gemini.
**Summarize Emails** — Paste a long email and get a 2–3 bullet point summary instantly. No more reading through walls of text.

## Tech used
- **Python + Flask** — handles the backend and serves the web pages
- **Google Gemini API** — the AI model that actually generates the answers
- **HTML, CSS, JavaScript** — the frontend, nothing fancy
- **python-dotenv** — keeps the API key out of the code
- **Gunicorn** — runs the app properly in production (Flask's built-in server isn't meant for real deployment)
- **Render** — where the app is hosted, connected directly to this GitHub repo

## Run it locally
You'll need Python 3.10+ and a [Gemini API key](https://aistudio.google.com/app/apikey).
```bash
git clone https://github.com/your-username/ai-personal-assistant.git
cd ai-personal-assistant
pip install -r requirements.txt
```

Create a `.env` file in the root folder:
```
google_api_key=your_key_here
```

Then run:
```bash
python main.py
```
Open `http://127.0.0.1:5000` in your browser.

## Project structure
```
ai-personal-assistant/
├── main.py              # Flask routes and Gemini API calls
├── requirements.txt     # Dependencies
├── .env                 # API key (never pushed to GitHub)
├── templates/
│   └── index.html       # Frontend UI
└── static/
    └── style.css        # Styling
```

## API Endpoints
`POST /ask` — send a question, get an answer back as JSON
`POST /summarize` — send email text, get a bullet-point summary back as JSON

## Why I built this
I wanted to build something that actually connects to a real AI model end-to-end — not just run a notebook. 
This project taught me how to wrap an LLM inside a web server, handle API keys securely, and ship it live on the internet. 
It's a small project but it covers the full cycle from writing the code to having a real URL you can share.

## Author
**Nitin Kumawat**
[LinkedIn](www.linkedin.com/in/nitin-ku04)
