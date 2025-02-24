# Handles Database Operations
from sqlalchemy.orm import Session
from . import models, schemas

def create_word(db: Session, word: schemas.WordCreate):
    db_word = models.Word(**word.dict())
    db.add(db_word)
    db.commit()
    db.refresh(db_word)
    return db_word

def get_word(db: Session, word_id: int):
    return db.query(models.Word).filter(models.Word.id == word_id).first()

def get_words(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Word).offset(skip).limit(limit).all()