import os

from fastapi import FastAPI

from app.api import experiment, health, user
from app.db import SQLModel, engine
from app.models.experiment_model import Experiment
from app.models.user_model import User


def create_application() -> FastAPI:
    application = FastAPI()

    application.include_router(health.router)
    application.include_router(user.router)
    application.include_router(experiment.router)

    return application


app = create_application()
