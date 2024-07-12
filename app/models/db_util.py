import sqlalchemy
from pydantic import BaseModel
import asyncio
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


async def async_main():
    print('1')
    # conn is an instance of AsyncConnection
    async with engine.begin() as conn:
        # to support SQLAlchemy DDL methods as well as legacy functions, the
        # AsyncConnection.run_sync() awaitable method will pass a "sync"
        # version of the AsyncConnection object to any synchronous method,
        # where synchronous IO calls will be transparently translated for
        # await.
        await conn.run_sync(meta.drop_all)
        await conn.run_sync(meta.create_all)

        # for normal statement execution, a traditional "await execute()"
        # pattern is used.
        await conn.execute(
            users.insert(), [{"id": "some id", "score": 10}, {"id": "some id2", "score": 8}]
        )

    async with engine.connect() as conn:
        # the default result object is the
        # sqlalchemy.engine.Result object
        result = await conn.execute(users.select())

        # the results are buffered so no await call is necessary
        # for this case.
        print(result.fetchall())

        # for a streaming result that buffers only segments of the
        # result at time, the AsyncConnection.stream() method is used.
        # this returns a sqlalchemy.ext.asyncio.AsyncResult object.
        async_result = await conn.stream(users.select())

        # this object supports async iteration and awaitable
        # versions of methods like .all(), fetchmany(), etc.
        async for row in async_result:
            print(row)


def run_database():
    print('124')
    asyncio.run(async_main())


class User(BaseModel):
    id: str
    score: int


class UserIn(BaseModel):
    score: int

