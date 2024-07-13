import asyncio

from fastapi import FastAPI
from app.routers import score_increment, get_user, root, user_download, user_upload, create_user
import uvicorn
from fastapi.middleware.cors import CORSMiddleware
from app.models.db_util import *


app = FastAPI()

# Allow CORS for all origins
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# adding routers
app.include_router(root.router)
app.include_router(user_download.router)
app.include_router(user_upload.router)
app.include_router(score_increment.router)
app.include_router(get_user.router)
app.include_router(create_user.router)


if __name__ == "__main__":
    asyncio.run(create_tables())
    uvicorn.run("main:app", host="127.0.0.1", port=3001, reload=False)
