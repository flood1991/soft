from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
import crud
from database import SessionLocal, Base, engine
from schemas import (UserSchema, GameSchema,
                     UserBase, GameBase
                     )
app = FastAPI()


def get_db():
    session = SessionLocal()
    try:
        yield session
        session.commit()
    finally:
        session.close()


Base.metadata.create_all(bind=engine)


@app.get("/users/", response_model=list[UserSchema])
def get_users(db: Session = Depends(get_db)):
    users = crud.get_me(db)
    return users


@app.post("/users/", response_model=UserBase)
def create_user(user: schemas.UserBase, db: Session = Depends(get_db)):
    return crud.create_user(db=db, user=user)


@app.get("/games/", response_model=list[GameSchema])
def get_games(db: Session = Depends(get_db)):
    games = crud.get_games(db)
    return games


@app.post("/games/", response_model=GameBase)
def create_game(game: schemas.GameBase, db: Session = Depends(get_db)):
    return crud.create_game(db=db, game=game)


@app.get("/connect/")
def connect_to_game(user_id: int, game_id: int,
                    db: Session = Depends(get_db)):
    return crud.connect_to_game(db=db, user_id=user_id, game_id=game_id)


