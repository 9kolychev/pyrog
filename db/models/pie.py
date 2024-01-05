from typing import TYPE_CHECKING

from sqlalchemy import String, Text, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import Base
from .mixins import UserRelationMixin

if TYPE_CHECKING:
    from .user import User


class Pie(UserRelationMixin, Base):
    # _user_id_nullable: bool = False
    # _user_id_unique: bool = False
    _user_back_populates = "pies"

    name: Mapped[str] = mapped_column(String(64), unique=True)
    description: Mapped[str] = mapped_column(
        Text,
        default="",
        server_default="",
    )
    nutritional_value: Mapped[str | None]

    # user_id: Mapped[int] = mapped_column(
    #     ForeignKey("users.id"),
    #     # nullable=False,
    # )
    # user: Mapped["User"] = relationship(back_populates="pies")
