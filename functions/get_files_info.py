import os
from google.genai import types

def get_files_info(working_directory, directory=None):
    working_dir_path = os.path.abspath(working_directory)
    ref = working_dir_path
    if directory:
        dir_path = os.path.abspath(os.path.join(working_directory, directory))
        ref = dir_path
    
    if not ref.startswith(working_dir_path):
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
    if not os.path.isdir(ref):
        return f'Error: "{directory}" is not a directory'
    
    try:
        contents = []
        for f in os.listdir(ref):
            fpath = os.path.join(ref, f)
            size = os.path.getsize(fpath)
            is_dir = os.path.isdir(fpath)
            contents.append(f"- {f}: file_size={size} bytes, is_dir={is_dir}")
        return "\n".join(contents)
    except Exception as e:
        return f"Error: could not get file contents: {e}"
    
schema_get_files_info = types.FunctionDeclaration(
    name="get_files_info",
    description="Lists files in the specified directory along with their sizes, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "directory": types.Schema(
                type=types.Type.STRING,
                description="The directory to list files from, relative to the working directory. If not provided, lists files in the working directory itself.",
            ),
        },
    ),
)