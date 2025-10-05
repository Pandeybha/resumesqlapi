from sqlalchemy import Column, Integer, String
from aap.database import Base

class Resume(Base):
    __tablename__ = "resumes"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    skills = Column(String, nullable=False)
    experience = Column(String, nullable=False)
