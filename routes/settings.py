from flask import Blueprint, render_template, request, redirect, url_for
from database.database import get_connection

settings_bp = Blueprint("settings", __name__)


@settings_bp.route("/settings", methods=["GET", "POST"])
def settings_home():
    conn = get_connection()
    try:
        user = conn.execute("SELECT * FROM users WHERE id = 1").fetchone()
        settings = conn.execute("SELECT * FROM settings WHERE user_id = 1").fetchone()
    finally:
        conn.close()

    if request.method == "POST":
        username = request.form.get("username", user["username"])
        theme = request.form.get("theme", settings["theme"])
        difficulty = request.form.get("difficulty", user["learning_difficulty"])
        conn = get_connection()
        try:
            conn.execute("UPDATE users SET username = ?, learning_difficulty = ? WHERE id = 1", (username, difficulty))
            conn.execute("UPDATE settings SET username = ?, theme = ?, learning_difficulty = ? WHERE user_id = 1", (username, theme, difficulty))
            conn.commit()
        finally:
            conn.close()
        return redirect(url_for("settings.settings_home"))

    return render_template("settings.html", user=user, settings=settings)
