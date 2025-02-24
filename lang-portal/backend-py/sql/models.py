from sqlalchemy import Column, Integer, String, JSON, ForeignKey, Boolean, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()

class Word(Base):
    __tablename__ = "words"

    id = Column(Integer, primary_key=True, index=True)
    thai = Column(String, nullable=False)  # Thai script
    english = Column(String, nullable=False)  # English translation
    parts = Column(JSON, nullable=False)  # Word components in JSON format
    correct_count = Column(Integer, default=0)  # Count of correct answers
    wrong_count = Column(Integer, default=0)  # Count of wrong answers

    # Many-to-many relationship with Group through WordGroup
    groups = relationship("Group", secondary="word_groups", back_populates="words")

class Group(Base):
    __tablename__ = "groups"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)  # Name of the group
    words_count = Column(Integer, default=0)  # Counter cache for the number of words in the group

    # Many-to-many relationship with Word through WordGroup
    words = relationship("Word", secondary="word_groups", back_populates="groups")

class WordGroup(Base):
    __tablename__ = "word_groups"

    word_id = Column(Integer, ForeignKey("words.id"), primary_key=True)  # Foreign key to Word
    group_id = Column(Integer, ForeignKey("groups.id"), primary_key=True)  # Foreign key to Group

class StudyActivity(Base):
    __tablename__ = "study_activities"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)  # Name of the study activity (e.g., "Flashcards", "Quiz")
    url = Column(String, nullable=False)  # URL of the study activity

class StudySession(Base):
    __tablename__ = "study_sessions"

    id = Column(Integer, primary_key=True, index=True)
    group_id = Column(Integer, ForeignKey("groups.id"), nullable=False)  # Foreign key to Group
    study_activity_id = Column(Integer, ForeignKey("study_activities.id"), nullable=False)  # Foreign key to StudyActivity
    created_at = Column(DateTime, default=datetime.utcnow)  # Timestamp of when the session was created

    # Relationships
    group = relationship("Group")
    study_activity = relationship("StudyActivity")
    word_review_items = relationship("WordReviewItem", back_populates="study_session")

class WordReviewItem(Base):
    __tablename__ = "word_review_items"

    id = Column(Integer, primary_key=True, index=True)
    word_id = Column(Integer, ForeignKey("words.id"), nullable=False)  # Foreign key to Word
    study_session_id = Column(Integer, ForeignKey("study_sessions.id"), nullable=False)  # Foreign key to StudySession
    correct = Column(Boolean, nullable=False)  # Whether the answer was correct
    created_at = Column(DateTime, default=datetime.utcnow)  # Timestamp of when the review occurred

    # Relationships
    word = relationship("Word")
    study_session = relationship("StudySession", back_populates="word_review_items")