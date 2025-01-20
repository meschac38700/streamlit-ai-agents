import json
from pathlib import Path

from models.pydantic import DialogList


def get_static_data(filepath: str | Path) -> DialogList:
    """Read and parse the given dataset filepath."""
    dataset_path = Path(filepath)
    if not dataset_path.exists():
        raise ValueError(f"Cannot found dataset file: {dataset_path}")

    with open(dataset_path) as f:
        data = json.loads(f.read())["troubleshooting_scenarios"]
        return DialogList(dialogs=data)
