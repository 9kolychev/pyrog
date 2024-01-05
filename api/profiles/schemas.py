from pydantic import BaseModel, ConfigDict, field_validator
from fastapi import HTTPException

import re

LETTER_MATCH_PATTERN = re.compile(r"^[а-яА-Яa-zA-Z\-]+$")


class ProfileBase(BaseModel):
    first_name: str
    last_name: str


class CreateProfile(ProfileBase):
    pass


class UpdatePie(CreateProfile):
    pass


class UpdatePiePartial(CreateProfile):
    first_name: str | None = None
    last_name: str | None = None

    @field_validator("first_name")
    def validate_name(cls, value):
        if not LETTER_MATCH_PATTERN.match(value):
            raise HTTPException(
                status_code=422, detail="First name should contains only letters"
            )
        return value

    @field_validator("last_name")
    def validate_surname(cls, value):
        if not LETTER_MATCH_PATTERN.match(value):
            raise HTTPException(
                status_code=422, detail="Last name should contains only letters"
            )
        return value


class Profile(ProfileBase):
    model_config = ConfigDict(from_attributes=True)
