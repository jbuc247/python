from flask import Blueprint, render_template, redirect, request, session, url_for

from database.database import get_connection
from services.progress import get_user


dashboard_bp = Blueprint("dashboard", __name__)


@dashboard_bp.route("/dashboard")
def dashboard_home():
    user = get_user()
    user_id = session["user_id"]
    conn = get_connection()
    try:
        challenge = conn.execute(
            "SELECT * FROM daily_challenges ORDER BY id LIMIT 1"
        ).fetchone()
        projects_completed = conn.execute(
            "SELECT COUNT(*) FROM project_attempts WHERE user_id = ? AND status = 'completed'",
            (user_id,),
        ).fetchone()[0]
        projects_total = conn.execute("SELECT COUNT(*) FROM projects").fetchone()[0]
    finally:
        conn.close()

    # Derive a current course from user's topic or fall back
    current_course = user.get("current_topic") or "Python Variables" if user else "Python Variables"
    course_progress = 0

    return render_template(
        "dashboard.html",
        user=user,
        challenge=challenge,
        current_course=current_course,
        course_progress=course_progress,
        todays_challenge=challenge["title"] if challenge else "No challenge today",
        projects_completed=projects_completed,
        projects_total=projects_total or 100,
        quiz_average=0,
    )


@dashboard_bp.route("/assessment", methods=["GET", "POST"])
def assessment():
    if request.method == "POST":
        session["assessment_done"] = True
        conn = get_connection()
        try:
            conn.execute(
                "UPDATE users SET assessment_done = 1 WHERE id = ?", (session["user_id"],)
            )
            conn.commit()
        finally:
            conn.close()
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
