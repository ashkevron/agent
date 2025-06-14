import os, subprocess
from google.genai import types

def run_python_file(working_directory, file_path):
    working_dir_abs = os.path.abspath(working_directory)
    file_path_abs = os.path.abspath(os.path.join(working_directory, file_path))
    
    if not file_path_abs.startswith(working_dir_abs):
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
    
    if not os.path.exists(file_path_abs):
        return f'Error: File "{file_path}" not found.'
    
    if not file_path_abs.endswith(".py"):
        return f'Error: "{file_path}" is not a Python file.'

    try:
        process = subprocess.run(["python3", file_path_abs], timeout=30, capture_output=True, cwd=working_dir_abs)
        if not process.stdout and not process.stderr:
            return "No output produced."
        message = f"STDOUT: {process.stdout.decode()}, STDERR: {process.stderr.decode()}"
        if process.returncode != 0:
            message += f", Process exited with code {process.returncode}"
        return message
    except Exception as e:
        return f"Error: executing Python file: {e}"
    
schema_run_python_file = types.FunctionDeclaration(
    name="run_python_file",
    description="Executes a Python file within the working directory and returns the output from the interpreter.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The path to the python file to execute, relative to the working directory.",
            ),
        },
    ),
)
