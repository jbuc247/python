from flask import Blueprint, render_template, request, redirect, session, url_for
from werkzeug.security import generate_password_hash, check_password_hash

from database.database import get_connection

auth_bp = Blueprint("auth", __name__)


@auth_bp.route("/signup", methods=["GET", "POST"])
def signup():
    if session.get("user_id"):
        return redirect(url_for("dashboard.dashboard_home"))

    error = None
    if request.method == "POST":
        username = request.form.get("username", "").strip()
        email = request.form.get("email", "").strip() or None
        password = request.form.get("password", "")
        confirm = request.form.get("confirm_password", "")

        if not username or not password:
            error = "Username and password are required."
        elif len(password) < 6:
            error = "Password must be at least 6 characters."
        elif password != confirm:
            error = "Passwords do not match."
        else:
            conn = get_connection()
            try:
                existing = conn.execute(
                    "SELECT id FROM users WHERE username = ?", (username,)
                ).fetchone()
                if existing:
                    error = "That username is already taken."
                else:
                    password_hash = generate_password_hash(password)
                    cursor = conn.execute(
                        """
                        INSERT INTO users (username, email, password_hash, level, xp, streak, learning_difficulty)
                        VALUES (?, ?, ?, 'Beginner', 0, 0, 'Beginner')
                        """,
                        (username, email, password_hash),
                    )
                    user_id = cursor.lastrowid
                    conn.execute(
                        """
                        INSERT INTO settings (user_id, theme, username, learning_difficulty, project_directory, terminal_shell)
                        VALUES (?, 'dark', ?, 'Beginner', 'user_projects', 'bash')
                        """,
                        (user_id, username),
                    )
                    conn.execute(
                        "INSERT INTO streaks (user_id, current_streak, best_streak) VALUES (?, 0, 0)",
                        (user_id,),
                    )
                    conn.commit()

                    session.clear()
                    session["user_id"] = user_id
                    session["username"] = username
                    return redirect(url_for("dashboard.assessment"))
            finally:
                conn.close()

    return render_template("signup.html", error=error)


@auth_bp.route("/login", methods=["GET", "POST"])
def login():
    if session.get("user_id"):
        return redirect(url_for("dashboard.dashboard_home"))

    error = None
    if request.method == "POST":
        username = request.form.get("username", "").strip()
        password = request.form.get("password", "")

        conn = get_connection()
        try:
            user = conn.execute(
                "SELECT * FROM users WHERE username = ?", (username,)
            ).fetchone()
        finally:
            conn.close()

        if user is None or not user["password_hash"] or not check_password_hash(
            user["password_hash"], password
        ):
            error = "Incorrect username or password."
        else:
            session.clear()
            session["user_id"] = user["id"]
            session["username"] = user["username"]
            session["assessment_done"] = bool(user["assessment_done"])
            next_url = request.args.get("next")
            if not session["assessment_done"]:
                return redirect(url_for("dashboard.assessment"))
            return redirect(next_url or url_for("dashboard.dashboard_home"))

    return render_template("login.html", error=error)


@auth_bp.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("auth.login"))
