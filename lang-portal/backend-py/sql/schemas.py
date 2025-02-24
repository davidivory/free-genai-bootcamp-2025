from pydantic import BaseModel
from typing import Dict

class WordBase(BaseModel):
    thai_script: str
    transliteration: str
    english: str
    parts: Dict[str, str]

class WordCreate(WordBase):
    pass  # Used for creating new words

class WordResponse(WordBase):
    id: int

    class Config:
        orm_mode = True  # Allows compatibility with SQLAlchemy models