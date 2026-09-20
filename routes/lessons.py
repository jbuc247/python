from flask import Blueprint, render_template, request
from database.database import get_connection

lessons_bp = Blueprint("lessons", __name__)


@lessons_bp.route("/lessons")
def lesson_list():
    conn = get_connection()
    try:
        lessons = conn.execute(
            "SELECT * FROM lessons ORDER BY order_index ASC"
        ).fetchall()
    finally:
        conn.close()
    return render_template("lessons.html", lessons=lessons)


@lessons_bp.route("/lesson/<slug>")
def lesson_detail(slug):
    conn = get_connection()
    try:
        lesson = conn.execute("SELECT * FROM lessons WHERE slug = ?", (slug,)).fetchone()
    finally:
        conn.close()
    if not lesson:
        return "Lesson not found", 404
    return render_template("lesson_detail.html", lesson=lesson)
