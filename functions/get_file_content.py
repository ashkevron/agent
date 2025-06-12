import os

def get_file_content(working_directory, file_path):
    working_dir_abs = os.path.abspath(working_directory)
    file_path_abs = os.path.abspath(os.path.join(working_directory, file_path))
    
    if not file_path_abs.startswith(working_dir_abs):
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
    if not os.path.isfile(file_path_abs):
        return f'Error: File not found or is not a regular file: "{file_path}"'
    
    try:
        MAX_CHARS = 10000
        with open(file_path_abs) as f:
            content = f.read(MAX_CHARS)
            if len(content) < MAX_CHARS:
                return content
            return f'{content}...File "{file_path}" truncated at {MAX_CHARS} characters'
    except Exception as e:
        return f'Error: could not read file: {e}'