import sqlalchemy
from pydantic import BaseModel
from sqlalchemy import MetaData
from sqlalchemy.ext.asyncio import create_async_engine

DATABASE_URL = "sqlite+aiosqlite:///sklep.db"

meta = MetaData()

users = sqlalchemy.Table(
    "users",
    meta,
    sqlalchemy.Column("user_id", sqlalchemy.String, primary_key=True),
    sqlalchemy.Column("score", sqlalchemy.Integer),
)


# engine is an instance of AsyncEngine
engine = create_async_engine(
        DATABASE_URL,
        echo=True,
    )


async def create_tables():
    print('tables created')
    async with engine.begin() as session:
        await session.run_sync(meta.create_all)


class User(BaseModel):
    user_id: str
    score: int
