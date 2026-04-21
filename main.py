from agent import Agent

agent = Agent()

print("AutoStream AI Agent Started... (type 'exit' to stop)")

while True:
    user = input("User: ")

    if user.lower() == "exit":
        break

    response = agent.run(user)
    print("Bot:", response)