from pathlib import Path

from utils import datasets


class AgentA:
    def __init__(self):
        filepath = Path(__file__).parent.parent / "datasets" / "static.json"
        self.data = datasets.get_static_data(filepath)

    def get_response(self, issue: str) -> str | None:
        return self.data.get(issue)
