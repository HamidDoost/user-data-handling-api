import logging
import os

from pydantic import BaseSettings


log=logging.getLogger("uvicorn")

# Defining Setting class for environemnt (dev, stage, prod) and test mode
class Settings(BaseSettings):
    environemnt:str=os.getenv("ENVIRONMENT", "dev")
    testing:bool=os.getenv("TESTING",0)
    

def get_settings()->BaseSettings:
    log.info("Loading config setting from the environemnt...")
    return Settings()
