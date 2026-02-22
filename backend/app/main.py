# main.py

from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session

from . import models, database, schemas, crud
from .game_logic import NumberGuessingGame

# Create database tables
models.Base.metadata.create_all(bind=database.engine)

app = FastAPI(title="Number Guessing API")

# CORS configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Dev only
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Global game instance
game = NumberGuessingGame()


# Dependency
def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()


# Health check
@app.get("/")
def health():
    return {"status": "API running"}


# Start new game
@app.post("/start")
def start_game():
    global game
    game = NumberGuessingGame()
    return {"message": "New game started"}


# Make guess
@app.post("/guess", response_model=schemas.GuessResponse)
def make_guess(request: schemas.GuessRequest):
    global game
    result = game.guess(request.number)

    return {
        "message": result,
        "attempts": game.attempts,
        "game_over": game.is_over
    }


# Save score
@app.post("/score", response_model=schemas.ScoreResponse)
def add_score(score: schemas.ScoreCreate, db: Session = Depends(get_db)):
    return crud.create_score(db, score)


# Leaderboard
@app.get("/leaderboard")
def leaderboard(db: Session = Depends(get_db)):
    return crud.get_scores(db)