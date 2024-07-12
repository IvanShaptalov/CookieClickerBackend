from sqlalchemy import select
from ..models.db_errors import *
from ..models.db_util import *
from typing import Optional


async def create_user(user: User, session) -> User:
    """for session use async with engine.begin() as session: """
    if await get_user_by_id(user.id, session=session) is not None:
        raise UserAlreadyExists()
    new_user = users.insert().values(id=user.id, score=user.score)
    await session.execute(new_user)
    await session.commit()
    return user


async def get_user_by_id(user_id: str, session) -> Optional[User]:
    result = await session.execute(select(users).where(users.c.id == user_id))
    user_row = result.scalars().first()
    if user_row is None:
        return None
    return user_row


async def increment_score(user_id: str, score: int, session):
    query = users.update().where(users.c.id == user_id).values(score=users.c.score + score)
    result = await session.execute(query)
    await session.commit()
    return result.rowcount
