import os

from openai import OpenAI

from models import Assistant, Chat, User

from agents import AgentA, AgentB  # isort: skip


def main():
    chat = Chat()
    chat.start_dialog()

    openai_api_key = os.getenv("OPENAI_API_KEY")
    model = os.getenv("OPENAI_MODEL") or "gpt-3.5-turbo"

    client = OpenAI(api_key=openai_api_key) if openai_api_key else None

    agent_a = AgentA()
    agent_b = AgentB(client, model)
    assistant = Assistant(agent_a, agent_b)

    user = User()
    if prompt := chat.prompt:
        user.write(chat, prompt)

        resolved = assistant.trigger_response(chat)

        if not resolved and client is None:
            chat.exit("Please check your OpenAI API key to continue.")


if __name__ == "__main__":
    main()
