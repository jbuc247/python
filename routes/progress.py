from flask import Blueprint, render_template
from services.progress import get_user

progress_bp = Blueprint("progress", __name__)


@progress_bp.route("/progress")
def progress_home():
    user = get_user()
    return render_template("progress.html", user=user)
