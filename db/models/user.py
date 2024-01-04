from typing import TYPE_CHECKING

from sqlalchemy import Uuid, String

from sqlalchemy import Column, Boolean, String
from sqlalchemy.orm import (
    relationship,
    mapped_column,
    declared_attr,
    Mapped,
    mapped_column,
)
from sqlalchemy.dialects.postgresql import UUID

import uuid

from .base import Base

if TYPE_CHECKING:
    from .pie import Pie
    from .profile import Profile


class User(Base):
    __tablename__ = "users"

    # user_id: Mapped[Uuid]
    # user_id: Mapped[str]
    username: Mapped[str] = mapped_column(String(32), unique=True)
    # is_active: Mapped[bool]

    # user_id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    # name = Column(String, nullable=False)
    # surname = Column(String, nullable=False)
    # email = Column(String, nullable=False, unique=True)
    # is_active = Column(Boolean(), default=True)

    pies: Mapped[list["Pie"]] = relationship(back_populates="user")
    profile: Mapped["Profile"] = relationship(back_populates="user")
