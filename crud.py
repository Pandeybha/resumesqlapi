from sqlalchemy.orm import Session
from aap import models, schemas

def create_resume(db: Session, resume: schemas.ResumeCreate):
    db_resume = models.Resume(**resume.dict())
    db.add(db_resume)
    db.commit()
    db.refresh(db_resume)
    return db_resume

def get_resumes(db: Session, skip: int = 0, limit: int = 50):
    return db.query(models.Resume).offset(skip).limit(limit).all()

def get_resume_by_id(db: Session, resume_id: int):
    return db.query(models.Resume).filter(models.Resume.id == resume_id).first()

def update_resume(db: Session, resume_id: int, resume: schemas.ResumeCreate):
    db_resume = db.query(models.Resume).filter(models.Resume.id == resume_id).first()
    if not db_resume:
        return None
    for key, value in resume.dict().items():
        setattr(db_resume, key, value)
    db.commit()
    db.refresh(db_resume)
    return db_resume

def delete_resume(db: Session, resume_id: int):
    db_resume = db.query(models.Resume).filter(models.Resume.id == resume_id).first()
    if not db_resume:
        return None
    db.delete(db_resume)
    db.commit()
    return db_resume
