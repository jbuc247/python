from database.database import get_connection


def ensure_user_exists():
    conn = get_connection()
    try:
        user = conn.execute("SELECT * FROM users WHERE id = 1").fetchone()
        if user is None:
            conn.execute(
                "INSERT INTO users (id, username, level, xp, streak, learning_difficulty) VALUES (1, 'Learner', 'Beginner', 0, 0, 'Beginner')"
            )
            conn.execute(
                "INSERT INTO settings (user_id, theme, username, learning_difficulty, project_directory, terminal_shell) VALUES (1, 'dark', 'Learner', 'Beginner', 'user_projects', 'bash')"
            )
            conn.execute(
                "INSERT INTO streaks (user_id, current_streak, best_streak) VALUES (1, 0, 0)"
            )
            conn.commit()
    finally:
        conn.close()


def get_user():
    conn = get_connection()
    try:
        user = conn.execute("SELECT * FROM users WHERE id = 1").fetchone()
        return dict(user) if user else None
    finally:
        conn.close()


def add_xp(points, source="lesson"):
    conn = get_connection()
    try:
        user = conn.execute("SELECT xp FROM users WHERE id = 1").fetchone()
        current_xp = user[0] if user else 0
        conn.execute("UPDATE users SET xp = ? WHERE id = 1", (current_xp + points,))
        conn.execute("INSERT INTO xp (user_id, points, source) VALUES (1, ?, ?)", (points, source))
        conn.commit()
    finally:
        conn.close()
