from flask import session

from database.database import get_connection


def current_user_id():
    """The logged-in user's id, or None if nobody is logged in."""
    return session.get("user_id")


def get_user():
    user_id = current_user_id()
    if not user_id:
        return None
    conn = get_connection()
    try:
        user = conn.execute("SELECT * FROM users WHERE id = ?", (user_id,)).fetchone()
        return dict(user) if user else None
    finally:
        conn.close()


def add_xp(points, source="lesson"):
    user_id = current_user_id()
    if not user_id:
        return
    conn = get_connection()
    try:
        user = conn.execute("SELECT xp FROM users WHERE id = ?", (user_id,)).fetchone()
        current_xp = user[0] if user else 0
        conn.execute("UPDATE users SET xp = ? WHERE id = ?", (current_xp + points, user_id))
        conn.execute(
            "INSERT INTO xp (user_id, points, source) VALUES (?, ?, ?)", (user_id, points, source)
        )
        conn.commit()
    finally:
        conn.close()
