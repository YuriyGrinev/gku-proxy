"""
    Test status
"""
from fastapi.testclient import TestClient

from src.core.main import app
from src.settings import settings


def test_answer():
    """
    Test answer
    """
    client = TestClient(app)
    result = client.get(settings.main_url)
    assert result.status_code == 200
    assert result.json() == {"status": "ok"}
