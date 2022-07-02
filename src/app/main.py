import os

from fastapi import FastAPI
from app.db import engine, SQLModel
from app.models.experiment_model import Experiment
from app.models.user_model import User
from app.api import health, user, experiment


def create_application() -> FastAPI:
    application = FastAPI()

    application.include_router(health.router)
    application.include_router(user.router)
    application.include_router(experiment.router)

    return application


app = create_application()