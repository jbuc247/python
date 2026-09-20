import os
from flask import Blueprint, render_template, request, redirect, url_for

from config import USER_PROJECTS_DIR
from database.database import get_connection
from services.evaluator import evaluate_project
from services.code_runner import run_python_code

projects_bp = Blueprint("projects", __name__)


@projects_bp.route("/projects")
def project_library():
    conn = get_connection()
    try:
        projects = conn.execute("SELECT * FROM projects ORDER BY id ASC").fetchall()
    finally:
        conn.close()
    return render_template("project_library.html", projects=projects)


@projects_bp.route("/project/<slug>", methods=["GET", "POST"])
def project_detail(slug):
    conn = get_connection()
    try:
        project = conn.execute("SELECT * FROM projects WHERE slug = ?", (slug,)).fetchone()
    finally:
        conn.close()
    if not project:
        return "Project not found", 404

    result = None
    execution = None
    if request.method == "POST":
        code = request.form.get("code", "")
        result = evaluate_project(project, code)
        execution = run_python_code(code)
    return render_template("project_detail.html", project=project, result=result, execution=execution)


@projects_bp.route("/workspace")
def workspace_home():
    projects = []
    if os.path.exists(USER_PROJECTS_DIR):
        for name in sorted(os.listdir(USER_PROJECTS_DIR)):
            path = os.path.join(USER_PROJECTS_DIR, name)
            if os.path.isdir(path):
                projects.append({"name": name, "path": path})
    return render_template("workspace.html", projects=projects)


@projects_bp.route("/workspace/create", methods=["POST"])
def create_project():
    name = request.form.get("name", "").strip()
    if name:
        project_dir = os.path.join(USER_PROJECTS_DIR, name)
        os.makedirs(project_dir, exist_ok=True)
        main_file = os.path.join(project_dir, "main.py")
        if not os.path.exists(main_file):
            with open(main_file, "w", encoding="utf-8") as f:
                f.write("print('Hello from your project!')\n")
    return redirect(url_for("projects.workspace_home"))
