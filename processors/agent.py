import os
from dotenv import load_dotenv
from pydantic_ai import Agent

# Variables if needed
_ = load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
if not OPENAI_API_KEY:
    raise RuntimeError('Missing OPENAI_API_KEY in .env')

# Agent setup
agent = Agent(
    model='gpt-4.1',
    system_prompt='Be concise, reply with one sentence',
    output_type=str
)

def call_agent(user_input: str):
    return agent.run_sync(f"{user_input}")  

"""
The first known use of "hello, world" was in a 1974 textbook about the C programming language.
"""

def main():
    print(call_agent("what is the capital of france").output)

if __name__ == "__main__":
    main()
