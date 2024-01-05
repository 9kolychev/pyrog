from fastapi import Depends, HTTPException, Form, status
from fastapi.routing import APIRouter
from sqlalchemy.ext.asyncio import AsyncSession

from db.models.session import db_helper
from auth import utils as auth_utils
from . import crud
from .schemas import CreateUser, UserSchema, TokenInfo

router = APIRouter()


@router.post(
    "/",
    response_model=dict,
    status_code=status.HTTP_201_CREATED,
)
async def create_user(
    user: CreateUser,
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    return await crud.create_user(
        session=session,
        user_in=user,
    )


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


@router.post("/login/", response_model=TokenInfo)
async def auth_user_issue_jwt(
    user: UserSchema = Depends(validate_auth_user),
):
    jwt_payload = {
        # subject
        "sub": user.username,
        "username": user.username,
        "email": user.email,
    }
    token = auth_utils.encode_jwt(jwt_payload)
    return TokenInfo(
        access_token=token,
        token_type="Bearer",
    )
