from fastapi import Depends, HTTPException, Form, status, Security
from fastapi.routing import APIRouter
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from sqlalchemy.ext.asyncio import AsyncSession

from db.models.session import db_helper
from auth import utils as auth_utils
from .dependencies import validate_auth_user
from . import crud
from .schemas import CreateUser, UserSchema, TokenInfo

router = APIRouter()

security = HTTPBearer()


@router.post(
    "/signup/",
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


@router.post("/delete/")
async def delete_user(
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
    credentials: HTTPAuthorizationCredentials = Security(security),
):
    token = credentials.credentials
    decode_jwt = auth_utils.decode_jwt(token)
    print(decode_jwt)
    if decode_jwt:
        return await crud.delete_user(
            session=session,
            user_in=decode_jwt.get("username"),
        )
    # return {
    #     "success": True,
    #     "message": "user successfully deleted",
    # }
