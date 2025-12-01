
from crewai import Task
from agents import (
    miscommunication_agent, sentiment_agent, grammar_agent,
    context_agent, suggested_reply_agent
)

miscommunication_task = Task(
    description=(
        "Analyze the message for miscommunication risks. Message: {text}\n"
        "Output:\n"
        "- Issues: (tone, ambiguity, conflicting instructions, missing context)\n"
        "- Why risky: 2-4 bullets with evidence quoted from text\n"
        "- Quick fixes: bullet list of specific edits"
    ),
    expected_output="Structured bullets for issues, why risky, and quick fixes.",
    agent=miscommunication_agent
)

sentiment_task = Task(
    description=(
        "Classify sentiment and emotion for: {text}\n"
        "Output:\n"
        "- Sentiment: Positive/Neutral/Negative\n"
        "- Emotions: up to 3 (e.g., frustrated, confident)\n"
        "- Evidence: 2-3 short quotes from text"
    ),
    expected_output="Short sentiment label, 1-3 emotions, and evidence quotes.",
    agent=sentiment_agent
)

grammar_task = Task(
    description=(
        "Review grammar, punctuation, and clarity for: {text}\n"
        "Output:\n"
        "- Issues: bullet list\n"
        "- Fixes: improved phrasing for each\n"
        "- One-paragraph clean rewrite"
    ),
    expected_output="List of issues + fixes + one clean rewrite paragraph.",
    agent=grammar_agent
)

context_task = Task(
    description=(
        "Detect missing information or unclear intent for: {text}\n"
        "Output:\n"
        "- What’s missing: bullets\n"
        "- Risks if missing: 2-3 bullets\n"
        "- Clarifying questions to ask"
    ),
    expected_output="Bullets for missing info, risks, and clear questions.",
    agent=context_agent
)

suggested_reply_task = Task(
    description=(
        "Write a short reply to the message: {text}\n"
        "Tone: {tone}. Goals: be clear, neutral, and professional.\n"
        "Include next steps and (if needed) 1-2 clarifying questions."
    ),
    expected_output="3-6 sentence reply that is polite and actionable.",
    agent=suggested_reply_agent
)
