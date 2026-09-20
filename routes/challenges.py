from flask import Blueprint, render_template, request
from database.database import get_connection

challenges_bp = Blueprint("challenges", __name__)


@challenges_bp.route("/challenges")
def challenge_home():
    conn = get_connection()
    try:
        challenges = conn.execute("SELECT * FROM daily_challenges ORDER BY id ASC").fetchall()
    finally:
        conn.close()
    return render_template("challenges.html", challenges=challenges)


@challenges_bp.route("/challenges/<int:challenge_id>")
def challenge_detail(challenge_id):
    conn = get_connection()
    try:
        challenge = conn.execute(
            "SELECT * FROM daily_challenges WHERE id = ?", (challenge_id,)
        ).fetchone()
    finally:
        conn.close()
    if not challenge:
        return "Challenge not found", 404
    return render_template("challenge_detail.html", challenge=challenge)
