from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..sql import schemas, crud, database

router = APIRouter()

@router.post("/words/", response_model=schemas.WordResponse)
def create_word(word: schemas.WordCreate, db: Session = Depends(database.get_db)):
    return crud.create_word(db, word)

@router.get("/words/{word_id}", response_model=schemas.WordResponse)
def read_word(word_id: int, db: Session = Depends(database.get_db)):
    word = crud.get_word(db, word_id)
    if word is None:
        raise HTTPException(status_code=404, detail="Word not found")
    return word

@router.get("/words/", response_model=list[schemas.WordResponse])
def read_words(skip: int = 0, limit: int = 10, db: Session = Depends(database.get_db)):
    return crud.get_words(db, skip, limit)