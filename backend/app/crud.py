# crud.py

# Import Session type
from sqlalchemy.orm import Session

# Import models and schemas
from . import models, schemas


# Create new score in database
def create_score(db: Session, score: schemas.ScoreCreate):

    # Convert schema into database model
    db_score = models.Score(
        player_name=score.player_name,
        attempts=score.attempts
    )

    # Add to database session
    db.add(db_score)

    # Commit transaction (execute SQL)
    db.commit()

    # Refresh object to get generated ID
    db.refresh(db_score)

    return db_score


# Get all scores
def get_scores(db: Session):

    return db.query(models.Score).all()