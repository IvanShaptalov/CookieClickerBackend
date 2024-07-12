import sqlalchemy
from pydantic import BaseModel
from sqlalchemy import MetaData
from sqlalchemy.ext.asyncio import create_async_engine

DATABASE_URL = "sqlite+aiosqlite:///test.db"

meta = MetaData()

users = sqlalchemy.Table(
    "users",
    meta,
    sqlalchemy.Column("id", sqlalchemy.String, primary_key=True),
    sqlalchemy.Column("score", sqlalchemy.Integer),
)


# engine is an instance of AsyncEngine
engine = create_async_engine(
        DATABASE_URL,
        echo=True,
    )


class User(BaseModel):
    id: str
    score: int


class UserIn(BaseModel):
    score: int

