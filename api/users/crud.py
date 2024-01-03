from fastapi import HTTPException
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from db.models import User
from .schemas import CreateUser
from auth import utils as auth_utils


async def get_user(session: AsyncSession, username: str) -> User | None:
    stmt = select(User).where(User.username == username)
    return await session.scalar(stmt)


async def create_user(session: AsyncSession, user_in: CreateUser) -> dict:
    user = User(
        username=user_in.username,
        password=auth_utils.hash_password(user_in.password),
        email=user_in.email,
        active=user_in.active,
    )
    session.add(user)
    await session.commit()
    return {
        "success": True,
    }


async def delete_user(session: AsyncSession, user_in: str) -> dict[str, str | bool]:
    stmt = select(User).where(User.username == user_in)
    user = await session.scalar(stmt)

    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    await session.delete(user)
    await session.commit()

    user = await session.scalar(stmt)

    if not user:
        return {
            "success": True,
            "message": "user successfully deleted",
        }
    else:
        raise HTTPException(status_code=404, detail="User not delete")
