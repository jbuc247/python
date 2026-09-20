import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
DB_PATH = BASE_DIR / "database" / "learning_lab.db"
USER_PROJECTS_DIR = BASE_DIR / "user_projects"
SECRET_KEY = os.environ.get("SECRET_KEY", "python-learning-lab-secret")
SESSION_COOKIE_NAME = "python_learning_lab_session"
HOST = os.environ.get("HOST", "127.0.0.1")
PORT = int(os.environ.get("PORT", "5000"))

USER_PROJECTS_DIR.mkdir(exist_ok=True, parents=True)
