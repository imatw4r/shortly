from fastapi import FastAPI

from shortly.app.signals import setup_signals

app = FastAPI()

setup_signals(app=app)
