from fastapi import FastAPI

from shortly.app.infra.db import SQLALCHEMY_ENGINE


def dispose_sqlalchemy_engine_event() -> None:
    SQLALCHEMY_ENGINE.dispose()


def setup_events(app: FastAPI) -> None:
    app.add_event_handler(event_type="shutdown", func=dispose_sqlalchemy_engine_event)
