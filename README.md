# Groq Tool-Calling Agent

A simple AI agent built with the Groq API that demonstrates the core **tool-calling / function-calling** pattern used in production GenAI systems.

The agent doesn't just chat — it decides when it needs external information (weather, math), calls the right tool itself, and uses the real result to answer accurately.

## How it works

1. User asks a question
2. The LLM decides whether it needs a tool to answer correctly
3. If yes, it requests a tool call (e.g. `get_weather(city="Hyderabad")`)
4. The Python code executes the actual function and returns the result
5. The LLM uses that real data to generate its final answer

This ask → decide → act → respond loop is the foundation behind every tool-using agent framework (LangChain, LangGraph, CrewAI).

## Tech Stack

- **Python**
- **Groq API** (`openai/gpt-oss-120b` model) — fast LLM inference
- **python-dotenv** — for secure API key handling

## Project Structure
groq_tool_agent/
├── tools.py # Tool functions (get_weather, calculator) + their schemas
├── agent.py # Core agent loop (tool-calling logic)
├── main.py # Entry point
├── requirements.txt
└── .env # API key (not committed)

## Setup & Run

```bash
# 1. Clone the repo
git clone https://github.com/ravikumarpanthangi/groq-tool-agent.git
cd groq-tool-agent

# 2. Create and activate a virtual environment
python -m venv venv
source venv/Scripts/activate   # Windows (Git Bash)
# source venv/bin/activate     # Mac/Linux

# 3. Install dependencies
pip install -r requirements.txt

# 4. Add your Groq API key
# Create a .env file in the project root:
echo "GROQ_API_KEY=your_key_here" > .env

# 5. Run it
python main.py
```

## Example

**Input:**
> "What's the weather in Hyderabad, and what's 45 * 12?"

**Agent behavior (visible in console):**

**Final output:**
> The current weather in Hyderabad is 32°C, humid, with a chance of rain in the evening. And 45 × 12 = 540.

## Next Steps

- Replace mock weather data with a real weather API
- Add more tools (web search, database queries)
- Extend into a multi-agent system with specialized agents