from typing import Annotated

from annotated_types import MinLen, MaxLen
from pydantic import BaseModel, EmailStr, ConfigDict


class PieBase(BaseModel):
    name: str
    description: str
    price: int


class CreatePie(PieBase):
    pass


class UpdatePie(CreatePie):
    pass


class UpdatePiePartial(CreatePie):
    name: str | None = None
    description: str | None = None
    price: int | None = None


class Pie(PieBase):
    model_config = ConfigDict(from_attributes=True)

    id: int
