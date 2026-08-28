import os
from dotenv import load_dotenv
from groq import Groq
from agent import run_agent

load_dotenv()

client = Groq(api_key=os.environ["GROQ_API_KEY"])

if __name__ == "__main__":
    question = "What's the weather in Hyderabad, and what's 45 * 12?"
    answer = run_agent(client, question)
    print(answer)