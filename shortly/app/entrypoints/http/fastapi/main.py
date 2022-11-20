from fastapi import FastAPI

from shortly.app.entrypoints.http.fastapi.middlewares import setup_middlewares
from shortly.app.entrypoints.http.fastapi.signals import setup_signals

app = FastAPI()

setup_signals(app=app)
setup_middlewares(app=app)
