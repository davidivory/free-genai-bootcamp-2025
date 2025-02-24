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