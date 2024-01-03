from fastapi import Depends, HTTPException, Form, status
from sqlalchemy.ext.asyncio import AsyncSession

from db.models.session import db_helper
from auth import utils as auth_utils
from . import crud


async def validate_auth_user(
    username: str = Form(),
    password: str = Form(),
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    unauthed_exc = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="invalid username or password",
    )

    users_db = await crud.get_user(session=session, username=username)

    if not users_db.username:
        raise unauthed_exc

    if not auth_utils.validate_password(
        password=password,
        hashed_password=users_db.password,
    ):
        raise unauthed_exc

    if not users_db.active:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="user inactive",
        )

    return users_db
