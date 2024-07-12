from fastapi import FastAPI
from contextlib import asynccontextmanager
from app.models.db_util import engine, run_database
import logging
from app.routers import score_increment, get_user, root, user_download, user_upload
import uvicorn


@asynccontextmanager
async def lifespan(app_param: FastAPI):
    # Open database connection
    logging.info('database connected')
    await engine.connect()
    yield
    # Close database connection
    await engine.disconnect()
    logging.info('database disconnected')

print('run async main')

# run_database()

app = FastAPI(lifespan=lifespan)

app.include_router(root.router)
app.include_router(user_download.router)
app.include_router(user_upload.router)
app.include_router(score_increment.router)
app.include_router(get_user.router)
print('*'*80)

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=5000, reload=False)