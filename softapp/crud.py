from sqlalchemy.orm import Session

import models
import schemas


def connect_to_game(db: Session, user_id: int, game_id: int):
    user = db.query(models.User).filter(id=user_id).first()
    game = db.query(models.Game).filter(id=game_id).first()
    if user and game:
        print('connect')
        user.games.append(game)
    return user


def get_games(db: Session):
    return db.query(models.Game).all()


def create_game(db: Session, game: schemas.GameBase):
    game = models.Game(name=game.name)
    db.add(game)
    db.commit()
    db.refresh(game)
    return game


def get_me(db: Session):
    return db.query(models.User).all()


def create_user(db: Session, user: schemas.UserBase):
    user = models.User(name=user.name, age=user.age, email=user.email)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user
