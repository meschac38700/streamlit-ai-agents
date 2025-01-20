from utils import datasets


class AgentA:
    def __init__(self):
        self.data = datasets.get_static_data()

    def get_response(self, issue: str) -> str | None:
        return self.data.get(issue)
