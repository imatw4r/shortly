from shortly.app import app
from shortly.app.config import settings


def test_example():
    assert app
    assert settings
