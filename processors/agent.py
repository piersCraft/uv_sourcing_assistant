from pydantic_ai import Agent
# Agent setup
agent = Agent(
    'gpt-4.1',
    system_prompt='Be concise, reply with one sentence',
)

result = agent.run_sync('Where does "hello world" come from?')

def main():
    print(result.output)


if __name__ == "__main__":
    main()
