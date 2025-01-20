from .chat import Chat
from .message import Message


class User:
    def write(self, chat: Chat, text: str):
        msg = Message(role="user", content=text)
        chat.add_message(msg)
