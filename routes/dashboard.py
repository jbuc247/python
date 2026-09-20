from flask import Blueprint, render_template, redirect, request, session, url_for

from database.database import get_connection
from services.progress import ensure_user_exists, get_user


dashboard_bp = Blueprint("dashboard", __name__)


@dashboard_bp.route("/dashboard")
def dashboard_home():
    ensure_user_exists()
    user = get_user()
    conn = get_connection()
    try:
        challenge = conn.execute(
            "SELECT * FROM daily_challenges ORDER BY id LIMIT 1"
        ).fetchone()
    finally:
        conn.close()
    return render_template("dashboard.html", user=user, challenge=challenge)


@dashboard_bp.route("/assessment", methods=["GET", "POST"])
def assessment():
    if request.method == "POST":
        session["assessment_done"] = True
        return redirect(url_for("dashboard.dashboard_home"))

    questions = [
        "Have you programmed before?",
        "Have you used Python?",
        "Do you understand variables?",
        "Do you understand if/else?",
        "Do you understand loops?",
        "Do you understand functions?",
        "Do you understand lists?",
        "Do you understand dictionaries?",
        "Do you understand classes?",
    ]
    return render_template("assessment.html", questions=questions)

