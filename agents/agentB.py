from typing import Iterable

from openai import OpenAI
from openai.types.chat import ChatCompletionMessageParam


class AgentB:
    def __init__(self, client: OpenAI | None, model: str):
        self.client = client
        self.model = model

    def get_response(
        self, messages: Iterable[ChatCompletionMessageParam]
    ) -> str | None:
        if self.client is None:
            return None

        response = self.client.chat.completions.create(
            model=self.model, messages=messages
        )

        return response.choices[0].message.content
