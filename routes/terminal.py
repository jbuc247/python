import os
import subprocess
from flask import Blueprint, render_template, request, jsonify
from config import Config

terminal_bp = Blueprint("terminal", __name__)

@terminal_bp.route("/terminal")
def terminal_home():
    return render_template("terminal.html", default_dir=Config.USER_PROJECTS_DIR)

@terminal_bp.route("/api/terminal/execute", methods=["POST"])
def terminal_execute():
    data = request.get_json()
    command = data.get("command", "").strip()
    cwd = data.get("cwd", Config.USER_PROJECTS_DIR)
    
    if not command:
        return jsonify({"output": "", "cwd": cwd})
        
    # Handle 'cd' internally since each command runs in a new subprocess
    if command.startswith("cd "):
        target_dir = command[3:].strip()
        # Handle 'cd ~' or relative paths
        if target_dir == '~':
            new_cwd = Config.USER_PROJECTS_DIR
        else:
            new_cwd = os.path.abspath(os.path.join(cwd, target_dir))
            
        if os.path.isdir(new_cwd):
            return jsonify({"output": "", "cwd": new_cwd})
        else:
            return jsonify({"output": f"cd: {target_dir}: No such file or directory", "cwd": cwd})
            
    try:
        # Run the command
        result = subprocess.run(
            command,
            shell=True,
            cwd=cwd,
            capture_output=True,
            text=True,
            timeout=10
        )
        
        output = result.stdout
        if result.stderr:
            output += result.stderr
            
        return jsonify({"output": output, "cwd": cwd})
    except subprocess.TimeoutExpired:
        return jsonify({"output": "Command timed out after 10 seconds.", "cwd": cwd})
    except Exception as e:
        return jsonify({"output": f"Error: {str(e)}", "cwd": cwd})
