from fastapi import FastAPI, Depends
from app.config import get_settings, Settings

app=FastAPI()

@app.get("/ping")
async def pong(settings: Settings = Depends(get_settings)):
    return {
        "ping":"pong",
        "envirnemnt":settings.environemnt,
        "testig":settings.testing
    }