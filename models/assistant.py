from typing import Iterable

from openai.types.chat import ChatCompletionMessageParam

from agents import AgentA, AgentB

from .chat import Chat
from .message import Message

OpenAIMessages = Iterable[ChatCompletionMessageParam]


class Assistant:
    def __init__(self, agent_a: AgentA, agent_b: AgentB):
        self.agent_a = agent_a
        self.agent_b = agent_b

    def write(self, chat: Chat, text: str):
        msg = Message(role="assistant", content=text)
        chat.add_message(msg)

    def trigger_response(self, chat: Chat) -> bool:
        msg = self.agent_response(chat)

        resolved = msg is not None
        if resolved:
            self.write(chat, msg)

        return resolved

    def agent_response(self, chat: Chat):
        if (msg := self._get_agent_a_response(chat.last_message)) is None:
            msg = self._get_agent_b_response(chat.all_messages)

        return msg

    def _get_agent_a_response(self, question: str) -> str | None:
        return self.agent_a.get_response(question)

    def _get_agent_b_response(self, messages: OpenAIMessages) -> str | None:
        return self.agent_b.get_response(messages)
