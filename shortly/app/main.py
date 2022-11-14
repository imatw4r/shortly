from fastapi import FastAPI

from shortly.app.events import setup_events

app = FastAPI()

setup_events(app=app)
