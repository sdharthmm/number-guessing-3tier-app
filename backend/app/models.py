# models.py

# Import Column types
from sqlalchemy import Column, Integer, String

# Import Base from database.py
from .database import Base


# This class represents a table in the database
class Score(Base):

    # Table name inside the database
    __tablename__ = "scores"

    # Primary key column
    id = Column(Integer, primary_key=True, index=True)

    # Player name column
    player_name = Column(String, index=True)

    # Number of attempts taken
    attempts = Column(Integer)