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

@router.get("/groups", response_model=list[schemas.Group])
def read_groups(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud.get_groups(db, skip=skip, limit=limit)
