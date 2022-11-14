from fastapi import FastAPI

from shortly.app.events import setup_events

app = FastAPI()

# setup FastAPI components

setup_events(app=app)
