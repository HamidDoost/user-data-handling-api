from fastapi import FastAPI, Depends
from app.config import get_settings, Settings
from app.db import engine, SQLModel, init_db
from app.models import Hero


app = FastAPI()

# creating tables at startup
@app.on_event("startup")
async def on_startup():
    await init_db()


@app.get("/ping")
async def pong(settings: Settings = Depends(get_settings)):
    return {
        "ping": "pong",
        "envirnemnt": settings.environemnt,
        "testig": settings.testing,
    }
