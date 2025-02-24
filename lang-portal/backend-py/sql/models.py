from sqlalchemy import Column, Integer, String, JSON
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Word(Base):
    __tablename__ = "words"

    id = Column(Integer, primary_key=True, index=True)
    thai_script = Column(String, nullable=False)  
    transliteration = Column(String, nullable=False) 
    english = Column(String, nullable=False)  # English translation
    parts = Column(JSON, nullable=False)  # Word components in JSON format