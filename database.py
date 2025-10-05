import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# Database URL ko environment variable se read karega
# Local run -> fallback: localhost
# Docker run -> docker-compose.yml ka DATABASE_URL use karega
SQLALCHEMY_DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "postgresql+psycopg2://postgres:bhawnapandey123@localhost:5432/resume_db"
)

# Create the engine
engine = create_engine(SQLALCHEMY_DATABASE_URL, future=True)

# Create a session
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base class for models
Base = declarative_base()

# Dependency for getting DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
