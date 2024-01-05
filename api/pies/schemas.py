from enum import Enum
from pydantic import BaseModel, ConfigDict


class NutritionalValue(Enum):
    Squirrels: str
    Fats: str
    Carbohydrates: str


class PieBase(BaseModel):
    user_id: int
    name: str
    description: str
    nutritional_value: str | None = None


class CreatePie(PieBase):
    pass


class UpdatePie(CreatePie):
    pass


class UpdatePiePartial(CreatePie):
    user_id: int | None = None
    name: str | None = None
    description: str | None = None
    nutritional_value: str | None = None


class Pie(PieBase):
    model_config = ConfigDict(from_attributes=True)

    id: int
