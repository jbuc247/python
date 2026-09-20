import sqlite3
from pathlib import Path

from config import DB_PATH


def get_connection():
    DB_PATH.parent.mkdir(parents=True, exist_ok=True)
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn


def init_database():
    conn = get_connection()
    try:
        conn.execute(
            """
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT NOT NULL DEFAULT 'learner',
                email TEXT,
                level TEXT DEFAULT 'Beginner',
                xp INTEGER DEFAULT 0,
                streak INTEGER DEFAULT 0,
                current_topic TEXT,
                learning_difficulty TEXT DEFAULT 'Beginner',
                assessment_done INTEGER DEFAULT 0,
                created_at TEXT DEFAULT CURRENT_TIMESTAMP
            )
            """
        )

        conn.execute(
            """
            CREATE TABLE IF NOT EXISTS lessons (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                slug TEXT UNIQUE,
                title TEXT,
                category TEXT,
                difficulty TEXT,
                description TEXT,
                content TEXT,
                summary TEXT,
                order_index INTEGER DEFAULT 0,
                created_at TEXT DEFAULT CURRENT_TIMESTAMP
            )
            """
        )

        conn.execute(
            """
            CREATE TABLE IF NOT EXISTS lesson_progress (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER,
                lesson_id INTEGER,
                status TEXT DEFAULT 'not_started',
                score INTEGER DEFAULT 0,
                attempts INTEGER DEFAULT 0,
                last_updated TEXT DEFAULT CURRENT_TIMESTAMP,
                UNIQUE(user_id, lesson_id)
            )
            """
        )

        conn.execute(
            """
            CREATE TABLE IF NOT EXISTS quizzes (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                slug TEXT UNIQUE,
                title TEXT,
                topic TEXT,
                difficulty TEXT,
                description TEXT,
                total_questions INTEGER DEFAULT 0,
                created_at TEXT DEFAULT CURRENT_TIMESTAMP
            )
            """
        )

        conn.execute(
            """
            CREATE TABLE IF NOT EXISTS quiz_questions (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                quiz_id INTEGER,
                question TEXT,
                options TEXT,
                correct_answer TEXT,
                explanation TEXT,
                question_type TEXT DEFAULT 'multiple_choice'
            )
            """
        )

        conn.execute(
            """
            CREATE TABLE IF NOT EXISTS quiz_attempts (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER,
                quiz_id INTEGER,
                score INTEGER,
                total INTEGER,
                percentage REAL,
                completed_at TEXT DEFAULT CURRENT_TIMESTAMP
            )
            """
        )

        conn.execute(
            """
            CREATE TABLE IF NOT EXISTS projects (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                slug TEXT UNIQUE,
                name TEXT,
                difficulty TEXT,
                category TEXT,
                description TEXT,
                skills TEXT,
                requirements TEXT,
                learning_objectives TEXT,
                hints TEXT,
                test_cases TEXT,
                extension_ideas TEXT,
                expected_behavior TEXT,
                solution TEXT
            )
            """
        )

        conn.execute(
            """
            CREATE TABLE IF NOT EXISTS project_attempts (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER,
                project_id INTEGER,
                score INTEGER,
                status TEXT DEFAULT 'not_started',
                completed_at TEXT DEFAULT CURRENT_TIMESTAMP
            )
            """
        )

        conn.execute(
            """
            CREATE TABLE IF NOT EXISTS daily_challenges (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT,
                difficulty TEXT,
                description TEXT,
                requirements TEXT,
                hints TEXT,
                solution TEXT,
                challenge_date TEXT
            )
            """
        )

        conn.execute(
            """
            CREATE TABLE IF NOT EXISTS challenge_attempts (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER,
                challenge_id INTEGER,
                score INTEGER,
                completed_at TEXT DEFAULT CURRENT_TIMESTAMP
            )
            """
        )

        conn.execute(
            """
            CREATE TABLE IF NOT EXISTS xp (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER,
                points INTEGER DEFAULT 0,
                source TEXT,
                created_at TEXT DEFAULT CURRENT_TIMESTAMP
            )
            """
        )

        conn.execute(
            """
            CREATE TABLE IF NOT EXISTS streaks (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER,
                current_streak INTEGER DEFAULT 0,
                best_streak INTEGER DEFAULT 0,
                updated_at TEXT DEFAULT CURRENT_TIMESTAMP
            )
            """
        )

        conn.execute(
            """
            CREATE TABLE IF NOT EXISTS weak_topics (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER,
                topic TEXT,
                score INTEGER DEFAULT 0,
                updated_at TEXT DEFAULT CURRENT_TIMESTAMP
            )
            """
        )

        conn.execute(
            """
            CREATE TABLE IF NOT EXISTS settings (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER,
                theme TEXT DEFAULT 'dark',
                username TEXT,
                learning_difficulty TEXT DEFAULT 'Beginner',
                project_directory TEXT,
                terminal_shell TEXT DEFAULT 'bash',
                daily_challenge_enabled INTEGER DEFAULT 1
            )
            """
        )

        conn.commit()
    finally:
        conn.close()
