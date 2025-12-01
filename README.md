
# Agentic Communication Analyzer (Flask + CrewAI + Gemini Flash 2.0)

Five-agent dashboard (dark UI) matching your screenshot:
- Miscommunication Agent
- Sentiment Agent
- Grammar Agent
- Context Inspector
- Suggested Reply Agent

## Run locally (Windows)

```powershell
cd agentic_comm_analyzer_flask
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
copy .env.example .env
notepad .env   # paste your real GOOGLE_API_KEY
python app.py
```

Open http://localhost:5000

## Render.com deploy
- Build: `pip install -r requirements.txt`
- Start: `gunicorn app:app`
- Add env: `GOOGLE_API_KEY`
