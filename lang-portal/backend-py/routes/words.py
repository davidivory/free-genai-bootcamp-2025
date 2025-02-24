from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
from ..sql import schemas, crud, database, models
from ..dependencies import get_db

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

@router.get("/words", response_model=List[schemas.Word])
def get_words(
    page: int = Query(1, ge=1),
    sort_by: str = Query("thai", regex="^(thai|english|correct_count|wrong_count)$"),
    order: str = Query("asc", regex="^(asc|desc)$"),
    db: Session = Depends(get_db)
):
    words = crud.get_words(db, page=page, sort_by=sort_by, order=order)
    return words