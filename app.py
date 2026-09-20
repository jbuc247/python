from flask import Flask, redirect, url_for, session, request

from config import HOST, PORT, SECRET_KEY
from database.database import init_database
from database.init_db import bootstrap_default_data
from routes.auth import auth_bp
from routes.dashboard import dashboard_bp
from routes.lessons import lessons_bp
from routes.quizzes import quizzes_bp
from routes.challenges import challenges_bp
from routes.projects import projects_bp
from routes.terminal import terminal_bp
from routes.progress import progress_bp
from routes.settings import settings_bp
from routes.mentor import mentor_bp
from routes.api import api_bp

# Endpoints reachable without being logged in.
PUBLIC_ENDPOINTS = {"auth.login", "auth.signup", "static"}


def create_app():
    app = Flask(__name__)
    app.config["SECRET_KEY"] = SECRET_KEY
    app.config["HOST"] = HOST
    app.config["PORT"] = PORT

    init_database()
    bootstrap_default_data()

    app.register_blueprint(auth_bp)
    app.register_blueprint(dashboard_bp)
    app.register_blueprint(lessons_bp)
    app.register_blueprint(quizzes_bp)
    app.register_blueprint(challenges_bp)
    app.register_blueprint(projects_bp)
    app.register_blueprint(terminal_bp)
    app.register_blueprint(progress_bp)
    app.register_blueprint(settings_bp)
    app.register_blueprint(mentor_bp)
    app.register_blueprint(api_bp)

    @app.before_request
    def require_login():
        if request.endpoint in PUBLIC_ENDPOINTS or request.endpoint is None:
            return None
        if not session.get("user_id"):
            return redirect(url_for("auth.login", next=request.path))
        return None

    @app.route("/")
    def index():
        if not session.get("user_id"):
            return redirect(url_for("auth.login"))
        if session.get("assessment_done"):
            return redirect(url_for("dashboard.dashboard_home"))
        return redirect(url_for("dashboard.assessment"))

    return app


app = create_app()


if __name__ == "__main__":
    app.run(host=HOST, port=PORT, debug=True)
