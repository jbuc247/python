import os
from flask import Blueprint, render_template, request, redirect, jsonify, url_for

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
    projects_dir = str(USER_PROJECTS_DIR)
    if os.path.exists(projects_dir):
        for name in sorted(os.listdir(projects_dir)):
            path = os.path.join(projects_dir, name)
            if os.path.isdir(path):
                projects.append({"name": name, "path": path})
    return render_template("workspace.html", projects=projects)


@projects_bp.route("/workspace/create", methods=["POST"])
def create_project():
    name = request.form.get("name", "").strip()
    if name:
        project_dir = os.path.join(str(USER_PROJECTS_DIR), name)
        os.makedirs(project_dir, exist_ok=True)
        main_file = os.path.join(project_dir, "main.py")
        if not os.path.exists(main_file):
            with open(main_file, "w", encoding="utf-8") as f:
                f.write("print('Hello from your project!')\n")
    return redirect(url_for("projects.workspace_home"))


@projects_bp.route("/workspace/files")
def list_files():
    project = request.args.get("project", "")
    project_dir = os.path.join(str(USER_PROJECTS_DIR), project)
    files = []
    if os.path.isdir(project_dir):
        for item in os.listdir(project_dir):
            if os.path.isfile(os.path.join(project_dir, item)):
                files.append(item)
    return jsonify({"files": files})


@projects_bp.route("/workspace/file", methods=["GET", "POST"])
def handle_file():
    project = request.args.get("project", "")
    filename = request.args.get("filename", "")
    file_path = os.path.join(str(USER_PROJECTS_DIR), project, filename)

    if request.method == "GET":
        if not os.path.exists(file_path):
            return jsonify({"error": "File not found"}), 404
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()
        return jsonify({"content": content})

    elif request.method == "POST":
        data = request.get_json()
        content = data.get("content", "")
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(content)
        return jsonify({"success": True})
