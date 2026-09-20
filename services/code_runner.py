import os
import re
import subprocess
import sys
import tempfile
from pathlib import Path

DANGEROUS_PATTERNS = [
    "os.system",
    "subprocess",
    "eval(",
    "exec(",
    "import os",
    "import shutil",
    "rm -rf",
    "del /s",
    "shutdown",
    "reboot",
    "chmod",
    "mkfs",
    "kill ",
]


def sanitize_code(code: str) -> str:
    lowered = code.lower()
    for pattern in DANGEROUS_PATTERNS:
        if pattern.lower() in lowered:
            raise ValueError(f"This code uses a restricted command or module: {pattern}")
    return code


def run_python_code(code: str, timeout_seconds: int = 6):
    try:
        sanitized = sanitize_code(code)
    except ValueError as exc:
        return {"success": False, "output": "", "error": str(exc), "type": "security"}

    script_dir = Path(tempfile.mkdtemp(prefix="python_lab_"))
    script_path = script_dir / "main.py"
    script_path.write_text(sanitized, encoding="utf-8")

    try:
        result = subprocess.run(
            [sys.executable, str(script_path)],
            capture_output=True,
            text=True,
            timeout=timeout_seconds,
            cwd=str(script_dir),
            env={**os.environ, "PYTHONPATH": str(script_dir)},
        )

        output = result.stdout.strip()
        error = result.stderr.strip()
        if result.returncode == 0:
            return {"success": True, "output": output, "error": "", "type": "program"}
        return {"success": False, "output": output, "error": error, "type": "error"}
    except subprocess.TimeoutExpired:
        return {"success": False, "output": "", "error": "Execution timed out. Your code may be stuck in an infinite loop.", "type": "timeout"}
    except Exception as exc:
        return {"success": False, "output": "", "error": f"Runtime error: {exc}", "type": "error"}
