from sqlalchemy import Column, ForeignKey, Integer, String, Table
from sqlalchemy.orm import relationship

from database import Base


association_table = Table(
    "usergame",
    Base.metadata,
    Column("user_id", ForeignKey("users.id"), primary_key=True),
    Column("game_id", ForeignKey("games.id"), primary_key=True),
)


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    email = Column(String, unique=True, index=True)
    age = Column(Integer)
    games = relationship("Game", secondary=association_table, back_populates="users")


class Game(Base):
    __tablename__ = "games"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    users = relationship("User", secondary=association_table, back_populates="games")


