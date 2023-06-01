from fastapi import FastAPI
from . import models
from .routes import router
from .database import engine
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(router)