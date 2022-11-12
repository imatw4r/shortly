from shortly.app import app
from shortly.app.config import Settings


def test_example():
    assert app
    assert Settings()
