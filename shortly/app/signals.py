from fastapi import FastAPI

from shortly.app.adapters import sqlalchemy


def dispose_sqlalchemy_engine_signal() -> None:
    sqlalchemy.ENGINE.dispose()


def setup_signals(app: FastAPI) -> None:
    app.add_event_handler(event_type="shutdown", func=dispose_sqlalchemy_engine_signal)
