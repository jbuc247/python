import sqlite3

from flask import Blueprint, render_template, request, redirect, session, url_for
from database.database import get_connection

settings_bp = Blueprint("settings", __name__)


@settings_bp.route("/settings", methods=["GET", "POST"])
def settings_home():
    user_id = session["user_id"]
    conn = get_connection()
    try:
        user = conn.execute("SELECT * FROM users WHERE id = ?", (user_id,)).fetchone()
        settings = conn.execute("SELECT * FROM settings WHERE user_id = ?", (user_id,)).fetchone()
    finally:
        conn.close()

    error = None
    if request.method == "POST":
        username = request.form.get("username", user["username"]).strip() or user["username"]
        theme = request.form.get("theme", settings["theme"])
        difficulty = request.form.get("difficulty", user["learning_difficulty"])
        conn = get_connection()
        try:
            conn.execute(
                "UPDATE users SET username = ?, learning_difficulty = ? WHERE id = ?",
                (username, difficulty, user_id),
            )
            conn.execute(
                "UPDATE settings SET username = ?, theme = ?, learning_difficulty = ? WHERE user_id = ?",
                (username, theme, difficulty, user_id),
            )
            conn.commit()
            session["username"] = username
        except sqlite3.IntegrityError:
            conn.rollback()
            error = "That username is already taken."
        finally:
            conn.close()

        if not error:
            return redirect(url_for("settings.settings_home"))

        conn = get_connection()
        try:
            user = conn.execute("SELECT * FROM users WHERE id = ?", (user_id,)).fetchone()
            settings = conn.execute("SELECT * FROM settings WHERE user_id = ?", (user_id,)).fetchone()
        finally:
            conn.close()

    return render_template("settings.html", user=user, settings=settings, error=error)
