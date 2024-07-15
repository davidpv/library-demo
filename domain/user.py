from dataclasses import dataclass
from uuid import UUID


@dataclass(frozen=True)
class UserId:
    value: UUID


@dataclass(frozen=True)
class UserName:
    value: str


@dataclass
class User:
    user_id: UserId
    user_name: UserName
