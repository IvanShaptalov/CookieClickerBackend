from fastapi import FastAPI
from contextlib import asynccontextmanager
from app.models.db_util import database
import logging


@asynccontextmanager
async def lifespan(app_param: FastAPI):
    # Open database connection
    logging.info('database connected')
    await database.connect()
    yield
    # Close database connection
    await database.disconnect()
    logging.info('database disconnected')


app = FastAPI(lifespan=lifespan)
