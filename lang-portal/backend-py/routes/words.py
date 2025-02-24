from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
import crud, schemas
from database import SessionLocal

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/words", response_model=list[schemas.Word])
def read_words(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud.get_words(db, skip=skip, limit=limit)