from typing import List
from pydantic import BaseModel, Field


class UserBase(BaseModel):
    name: str
    email: str
    age: int = Field(ge=0, le=100)

    class Config:
        orm_mode = True


class GameBase(BaseModel):
    name: str

    class Config:
        orm_mode = True


class UserSchema(UserBase):
    games: List[GameBase]


class GameSchema(GameBase):
    users: List[UserBase]






