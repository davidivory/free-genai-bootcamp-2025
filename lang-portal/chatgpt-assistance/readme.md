## 🚀 Step 1: Open the VS Code Terminal
 Open Visual Studio Code.
Click on Terminal → New Terminal (or press Ctrl + ~).
Ensure you're in the correct project folder:
bash
Copy
Edit
cd path/to/your/project

## 🛠️ Step 2: Activate Your Virtual Environment
Run the command that matches your OS:

Windows (PowerShell)

powershell
Copy
Edit
venv\Scripts\Activate
Mac/Linux

bash
Copy
Edit
source venv/bin/activate
You should see (venv) at the beginning of the terminal line, confirming that your virtual environment is active.

## 📦 Step 3: Install Dependencies
Inside your VS Code terminal, install the required Python libraries:

bash
Copy
Edit
pip install fastapi uvicorn sqlalchemy alembic pydantic
To verify the installation:

bash
Copy
Edit
pip list
You should see FastAPI, SQLAlchemy, Uvicorn, and Pydantic listed.

## 📂 Step 4: Create and Organize Files
Now, create the project structure. You can create these files manually or use the following terminal commands:

bash
Copy
Edit
mkdir backend
cd backend
touch main.py database.py models.py schemas.py crud.py
mkdir routes
touch routes/words.py routes/groups.py routes/study_sessions.py
mkdir migrations
touch .env
For Windows PowerShell, use:

powershell
Copy
Edit
New-Item -ItemType File -Path main.py, database.py, models.py, schemas.py, crud.py, .env
New-Item -ItemType Directory -Path routes, migrations
New-Item -ItemType File -Path routes/words.py, routes/groups.py, routes/study_sessions.py

## 🛠️ Step 5: Initialize the Database
Once you've added the code for database.py, models.py, and schemas.py, run the following command inside the VS Code terminal to create the database:

bash
Copy
Edit
python -c "import models, database; models.Base.metadata.create_all(bind=database.engine)"
This will generate the learning.db SQLite database in your project folder.

## 🚀 Step 6: Start the FastAPI Server
Now, start your FastAPI application using:

bash
Copy
Edit
uvicorn main:app --reload
You should see an output similar to:

pgsql
Copy
Edit
INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)

## 🔍 Step 7: Test the API
Open your browser and go to:

arduino
Copy
Edit
http://127.0.0.1:8000/docs
You'll see FastAPI's interactive Swagger UI, where you can test the endpoints.

## ✨ Next Steps
If you face import errors, make sure your VS Code workspace is open at the backend folder.
If uvicorn doesn't run, try reinstalling dependencies:
bash
Copy
Edit
pip install --force-reinstall fastapi uvicorn sqlalchemy alembic pydantic
If you need auto-reloading on file changes, keep --reload in the command.

# Steps pt 2

## Step 1: Install Dependencies
In vscode terminal, activate virtual environment

pip install fastapi uvicorn sqlalchemy sqlite alembic pydantic
This installs:

FastAPI – for building APIs
Uvicorn – for running the API server
SQLAlchemy – for database ORM
SQLite – for the database
Alembic – for database migrations
Pydantic – for request validation

## Step 2: Project Structure
Create the following directory structure inside your project:

bash
Copy
Edit
/your_project
│── /app
│   │── main.py
│   │── database.py
│   │── models.py
│   │── schemas.py
│   │── crud.py
│   │── routes/
│   │   │── words.py
│   │   │── groups.py
│   │   │── sessions.py
│── alembic.ini  # Alembic configuration
│── requirements.txt
│── .env         # Environment variables (if needed)

## Step 3: Set Up the Database Connection (database.py)
Create a file called database.py inside the app/ directory.

python
Copy
Edit
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

DATABASE_URL = "sqlite:///./database.db"

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

## Step 4: Define the Database Models (models.py)
Create a file called models.py inside app/ and define your database schema.

python
Copy
Edit
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, JSON, TIMESTAMP
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from .database import Base

class Word(Base):
    __tablename__ = "words"

    id = Column(Integer, primary_key=True, index=True)
    thai = Column(String, nullable=False)
    phonetic = Column(String, nullable=False)
    english = Column(String, nullable=False)
    parts = Column(JSON, nullable=False)

    word_groups = relationship("WordGroup", back_populates="word")

class Group(Base):
    __tablename__ = "groups"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    words_count = Column(Integer, default=0)

    word_groups = relationship("WordGroup", back_populates="group")

class WordGroup(Base):
    __tablename__ = "word_groups"

    word_id = Column(Integer, ForeignKey("words.id"), primary_key=True)
    group_id = Column(Integer, ForeignKey("groups.id"), primary_key=True)

    word = relationship("Word", back_populates="word_groups")
    group = relationship("Group", back_populates="word_groups")

class StudyActivity(Base):
    __tablename__ = "study_activities"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    url = Column(String, nullable=False)

class StudySession(Base):
    __tablename__ = "study_sessions"

    id = Column(Integer, primary_key=True, index=True)
    group_id = Column(Integer, ForeignKey("groups.id"))
    study_activity_id = Column(Integer, ForeignKey("study_activities.id"))
    created_at = Column(TIMESTAMP, server_default=func.now())

class WordReviewItem(Base):
    __tablename__ = "word_review_items"

    id = Column(Integer, primary_key=True, index=True)
    word_id = Column(Integer, ForeignKey("words.id"))
    study_session_id = Column(Integer, ForeignKey("study_sessions.id"))
    correct = Column(Boolean, nullable=False)
    created_at = Column(TIMESTAMP, server_default=func.now())

## Step 5: Create Database Tables
Run the following command in the terminal to initialize Alembic migrations:

sh
Copy
Edit
alembic init alembic
Then, in alembic/env.py, find this line:

python
Copy
Edit
target_metadata = None
And change it to:

python
Copy
Edit
from app.database import Base
target_metadata = Base.metadata
Generate a migration script:

sh
Copy
Edit
alembic revision --autogenerate -m "Initial migration"
Apply the migration:

sh
Copy
Edit
alembic upgrade head

## Step 6: Define API Schemas (schemas.py)
Create schemas.py inside app/:

python
Copy
Edit
from pydantic import BaseModel
from typing import Optional

class WordSchema(BaseModel):
    thai: str
    phonetic: str
    english: str
    parts: dict

class GroupSchema(BaseModel):
    name: str

class StudySessionSchema(BaseModel):
    group_id: int
    study_activity_id: int

class WordReviewSchema(BaseModel):
    word_id: int
    correct: bool

## Step 7: Define CRUD Operations (crud.py)
Create crud.py in app/:

python
Copy
Edit
from sqlalchemy.orm import Session
from . import models, schemas

def get_words(db: Session):
    return db.query(models.Word).all()

def get_groups(db: Session):
    return db.query(models.Group).all()

def create_study_session(db: Session, session_data: schemas.StudySessionSchema):
    new_session = models.StudySession(
        group_id=session_data.group_id,
        study_activity_id=session_data.study_activity_id
    )
    db.add(new_session)
    db.commit()
    db.refresh(new_session)
    return new_session

## Step 8: Create API Routes
Inside app/routes/words.py:

python
Copy
Edit
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..database import SessionLocal
from .. import crud, schemas

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/words", response_model=list[schemas.WordSchema])
def get_words(db: Session = Depends(get_db)):
    return crud.get_words(db)
Inside app/routes/groups.py:

python
Copy
Edit
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..database import SessionLocal
from .. import crud, schemas

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/groups", response_model=list[schemas.GroupSchema])
def get_groups(db: Session = Depends(get_db)):
    return crud.get_groups(db)

## Step 9: Start the FastAPI App (main.py)
Create main.py in app/:

python
Copy
Edit
from fastapi import FastAPI
from .routes import words, groups

app = FastAPI()

app.include_router(words.router, prefix="/api")
app.include_router(groups.router, prefix="/api")

@app.get("/")
def read_root():
    return {"message": "Thai Learning API"}
Step 10: Run the Server
Run the FastAPI server:

sh
Copy
Edit
uvicorn app.main:app --reload
Your API will now be accessible at:

cpp
Copy
Edit
http://127.0.0.1:8000

Test it with:

arduino
Copy
Edit
http://127.0.0.1:8000/api/words
