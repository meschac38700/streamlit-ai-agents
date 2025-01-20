from pathlib import Path

from models.pydantic import DialogList
from utils.datasets import get_static_data


def test_get_static_data():
    filepath = Path(__file__).parent / "dataset.json"
    result = get_static_data(filepath)

    assert isinstance(result, DialogList)
    assert 2 == len(result)
    assert result.get("Computer won't turn on") is not None
    assert result.get("No internet connection") is not None
