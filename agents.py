
import os
from dotenv import load_dotenv
from crewai import Agent, LLM

load_dotenv()

# Native Google GenAI provider (avoid LiteLLM fallback)
llm = LLM(
    provider="google-genai",
    model="gemini/gemini-2.0-flash",
    api_key=os.getenv("GOOGLE_API_KEY")
)

miscommunication_agent = Agent(
    role="Miscommunication Agent",
    goal="Detect ambiguity, tone issues, and unclear meaning. Explain the risks and give fixes.",
    backstory="A pragmatic communication audit expert for workplace messages.",
    llm=llm
)

sentiment_agent = Agent(
    role="Sentiment Agent",
    goal="Classify overall sentiment and emotions with short evidence.",
    backstory="A lightweight sentiment and emotion classifier for text.",
    llm=llm
)

grammar_agent = Agent(
    role="Grammar Agent",
    goal="Find grammar, punctuation, and clarity issues; propose concise fixes.",
    backstory="An editor who prioritizes readability and correctness.",
    llm=llm
)

context_agent = Agent(
    role="Context Inspector",
    goal="Detect missing information or unclear intent; list specific clarifying questions.",
    backstory="A requirements-gathering specialist who reduces misinterpretation.",
    llm=llm
)

suggested_reply_agent = Agent(
    role="Suggested Reply Agent",
    goal="Generate a clean, neutral, and professional reply that resolves the detected issues.",
    backstory="An assistant that writes diplomatic and actionable responses.",
    llm=llm
)
