from pydantic import BaseModel, field_validator, Field, EmailStr

from tests.src.enums import Genders, Statuses


class PieModel(BaseModel):
    user_id: int
    name: str
    description: str
    nutritional_value: str
    # name: str = Field(alias="_name")


class Pie(PieModel):
    # id: int = Field(le=2)  # == check_id()
    id: int

    @field_validator("id")
    def check_id(cls, v):
        if v > 3:
            raise ValueError("Id is not less than two")
        else:
            return v
