from typing import Any

from pydantic import BaseModel, Field


class Dialog(BaseModel):
    issue: str
    steps: list[str]

    def steps_to_string(self) -> str:
        return "- " + "\n- ".join(self.steps)


class DialogList(BaseModel):
    dialogs: list[Dialog]
    dialog_mapping: dict[str, Dialog] = Field(init=False, default_factory=dict)

    def model_post_init(self, __context: Any) -> None:
        self.dialog_mapping = {dialog.issue: dialog for dialog in self.dialogs}

    def get(self, key: str) -> str | None:
        if key not in self.dialog_mapping:
            return None

        return self.dialog_mapping[key].steps_to_string()

    def __len__(self) -> int:
        return len(self.dialogs)
