from flask import Blueprint, request, jsonify

from services.code_runner import run_python_code

api_bp = Blueprint("api", __name__, url_prefix="/api")


@api_bp.route("/execute", methods=["POST"])
def execute_code():
    data = request.get_json(silent=True) or {}
    code = data.get("code", "")
    if not code:
        return jsonify({"error": "No code provided"}), 400
    return jsonify(run_python_code(code))
