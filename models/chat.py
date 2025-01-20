from typing import Iterable, NoReturn

import streamlit as stl
from openai.types.chat import ChatCompletionMessageParam

from .message import Message


class Chat:
    def __init__(
        self,
        *,
        title: str = "💬 Chatbot",
        assistant_message: str = "How can I help you?",
    ) -> None:
        self.messages: list[Message] = []
        self.set_title(title)
        self.start_message = Message(
            role="assistant",
            content=assistant_message,
        )
        self.last_message: str = ""

    def _initialization_(self) -> None:
        if "messages" not in stl.session_state:
            stl.session_state["messages"] = [self.start_message]

        # display session messages
        for msg in stl.session_state.messages:
            stl.chat_message(msg["role"]).markdown(msg["content"])

    def start_dialog(self):
        self._initialization_()

    def set_title(self, title: str) -> None:
        stl.title(title)

    @property
    def all_messages(self) -> Iterable[ChatCompletionMessageParam]:
        return stl.session_state.messages

    @property
    def prompt(self) -> None | str:
        return stl.chat_input()

    def add_message(self, message: Message) -> None:
        self.last_message = message["content"]
        stl.session_state.messages.append(message)
        stl.chat_message(message["role"]).markdown(message["content"])

    def exit(self, msg: str | None = None) -> NoReturn:
        if msg is not None:
            stl.info(msg)
        return stl.stop()
