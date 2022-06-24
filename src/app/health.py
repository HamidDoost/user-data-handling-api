# Server sanity ckeck router

from fastapi import FastAPI

app = FastAPI()


@app.get("/ping")
def pong():
    return {"message": "pong!"}
