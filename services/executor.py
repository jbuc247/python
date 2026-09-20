import subprocess
import tempfile
import os

def execute_python_code(code: str, timeout: int = 5) -> dict:
    """
    Executes Python code in a separate process.
    Returns a dict with 'stdout', 'stderr', and 'success'.
    """
    # Create a temporary file to hold the code
    with tempfile.NamedTemporaryFile(mode='w', suffix='.py', delete=False) as temp_file:
        temp_file.write(code)
        temp_file_path = temp_file.name

    try:
        # Run the code
        result = subprocess.run(
            ['python', temp_file_path],
            capture_output=True,
            text=True,
            timeout=timeout
        )
        return {
            'stdout': result.stdout,
            'stderr': result.stderr,
            'success': result.returncode == 0
        }
    except subprocess.TimeoutExpired:
        return {
            'stdout': '',
            'stderr': f'Execution timed out after {timeout} seconds. Check for infinite loops.',
            'success': False
        }
    except Exception as e:
        return {
            'stdout': '',
            'stderr': f'Internal Error: {str(e)}',
            'success': False
        }
    finally:
        # Clean up the temp file
        if os.path.exists(temp_file_path):
            os.remove(temp_file_path)
