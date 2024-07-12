import databases
import sqlalchemy
from pydantic import BaseModel


DATABASE_URL = "sqlite:///./app/models/test.db"

database = databases.Database(DATABASE_URL)

metadata = sqlalchemy.MetaData()

users = sqlalchemy.Table(
    "users",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.String, primary_key=True),
    sqlalchemy.Column("score", sqlalchemy.Integer),
)


engine = sqlalchemy.create_engine(
    DATABASE_URL, connect_args={"check_same_thread": False}
)
metadata.create_all(engine)


class User(BaseModel):
    id: str
    score: int


class UserIn(BaseModel):
    score: int




