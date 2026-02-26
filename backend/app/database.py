# database.py

# create_engine is used to connect to the database
from sqlalchemy import create_engine

# declarative_base is used to create a base class for our models
from sqlalchemy.ext.declarative import declarative_base

# sessionmaker creates database sessions
from sqlalchemy.orm import sessionmaker


# SQLite database URL
# "sqlite:///" means local file-based database
DATABASE_URL = "sqlite:///./data/scores.db"


# Engine is the core interface to the database
# check_same_thread=False is required for SQLite with FastAPI
engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False}
)


# SessionLocal will create new DB sessions
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)


# Base class that all models will inherit from
Base = declarative_base()