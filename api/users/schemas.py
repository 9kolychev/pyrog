from typing import Annotated

from annotated_types import MinLen, MaxLen
from pydantic import BaseModel, EmailStr, ConfigDict

import uuid


class TunedModel(BaseModel):
    class Config:
        """tells pydantic to convert even non dict obj to json"""

        from_attributes = True


class ShowUser(TunedModel):
    # user_id: uuid.UUID
    name: str
    surname: str
    email: EmailStr
    is_active: bool


class CreateUser(BaseModel):
    username: Annotated[str, MinLen(3), MaxLen(20)]
    email: EmailStr | None = None
    password: Annotated[str, MinLen(6), MaxLen(100)]
    active: bool = True


class UserSchema(BaseModel):
    model_config = ConfigDict(strict=True)
    username: str
    password: bytes
    email: EmailStr | None = None
    active: bool = True


class TokenInfo(BaseModel):
    access_token: str
    token_type: str