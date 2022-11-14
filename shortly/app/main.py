from fastapi import FastAPI

from shortly.app.middlewares import setup_middlewares
from shortly.app.signals import setup_signals

app = FastAPI()

setup_signals(app=app)
setup_middlewares(app=app)
