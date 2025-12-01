
import os
from flask import Flask, render_template, request, redirect, url_for, flash
from dotenv import load_dotenv
from crewai import Crew
from agents import (
    miscommunication_agent, sentiment_agent, grammar_agent,
    context_agent, suggested_reply_agent
)
from tasks import (
    miscommunication_task, sentiment_task, grammar_task,
    context_task, suggested_reply_task
)

load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv("FLASK_SECRET", "dev-secret")

# Build five separate crews (clear separation + fast kickoff)
crews = {
    "miscommunication": Crew(agents=[miscommunication_agent], tasks=[miscommunication_task]),
    "sentiment": Crew(agents=[sentiment_agent], tasks=[sentiment_task]),
    "grammar": Crew(agents=[grammar_agent], tasks=[grammar_task]),
    "context": Crew(agents=[context_agent], tasks=[context_task]),
    "suggested": Crew(agents=[suggested_reply_agent], tasks=[suggested_reply_task]),
}

@app.route("/", methods=["GET"])
def home():
    return render_template("dashboard.html")

@app.route("/run/<agent>", methods=["POST"])
def run_agent(agent):
    text = request.form.get("text", "").strip()
    tone = request.form.get("tone", "professional").strip()
    if not text:
        flash("Please paste a message to analyze.", "error")
        return redirect(url_for("home"))

    if agent not in crews:
        flash("Unknown agent selected.", "error")
        return redirect(url_for("home"))

    inputs = {"text": text, "tone": tone}
    try:
        result = crews[agent].kickoff(inputs=inputs)
    except Exception as e:
        result = f"⚠️ Error while running agent: {e}"

    return render_template("result.html", agent=agent, text=text, tone=tone, result=result)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)), debug=True)
