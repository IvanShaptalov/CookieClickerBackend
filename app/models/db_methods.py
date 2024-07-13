from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from ..models.db_errors import *
from ..models.db_util import *
from sqlalchemy import update


async def create_user(user: User, session: AsyncSession) -> User:
    """for session use async with engine.begin() as session: """
    user_already_exists = await get_user_by_id(user.user_id, session=session) is not None
    if user_already_exists:
        raise UserAlreadyExists

    new_user = users.insert().values(user_id=user.user_id, score=user.score)
    await session.execute(new_user)
    await session.commit()
    return user


async def get_user_by_id(user_id: str, session: AsyncSession) -> User | None:
    """load user from database, session must be opened - check create_user function for more details"""
    result = await session.execute(select(users).where(users.c.user_id == user_id))

    user_row = result.fetchone()
    if user_row is None:
        return None

    user_id = user_row[0]
    score = user_row[1]

    return User(user_id=user_id, score=score)


async def increment_score(user_id: str, score: int, session: AsyncSession):
    """increment user score"""
    result = await session.execute(select(users.c.user_id, users.c.score).where(users.c.user_id == user_id))
    user_row = result.fetchone()

    if user_row is None:
        raise UserNotFoundError(f"User with id {user_id} not found")

    # Update the user's score
    new_score = user_row[1] + score
    query = update(users).where(users.c.user_id == user_id).values(score=new_score)
    await session.execute(query)
    await session.commit()

    return User(user_id=user_row[0], score=new_score)
