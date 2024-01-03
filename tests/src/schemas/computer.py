from pydantic import BaseModel, HttpUrl, UUID4, field_validator, Field, EmailStr
from pydantic.types import PastDate, FutureDate, List, PaymentCardNumber
from pydantic.networks import IPv4Address, IPv6Address
from pydantic.color import Color


from tests.src.enums.user_enums import Statuses


class PhysicalInfo(BaseModel):
    color: Color
    photo: HttpUrl
    uuid: UUID4


class OwnersInfo(BaseModel):
    name: str
    card_number: PaymentCardNumber
    email: EmailStr


class DetailedInfo(BaseModel):
    physical: PhysicalInfo
    owners: List[OwnersInfo]


class Computer(BaseModel):
    status: Statuses
    activated_at: PastDate
    expiration_at: FutureDate
    host_v4: IPv4Address
    host_v6: IPv6Address
    detailed_info: DetailedInfo
