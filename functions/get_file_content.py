import os
from config import MAX_CHARS
from google.genai import types

def get_file_content(working_directory, file_path):
    try:
        working_dir_abs = (os.path.abspath(working_directory))
        target_dir = os.path.normpath(os.path.join(working_dir_abs, file_path))
        
        # Will be True or False
        valid_target_dir = os.path.commonpath([working_dir_abs, target_dir]) == working_dir_abs
        
        if not valid_target_dir:
            return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
        
        if not os.path.isfile(target_dir):
                return f'Error: File not found or is not a regular file: "{file_path}"'
            
        #f = open(target_dir)
        #what_read = f.read(MAX_CHARS)
        # After reading the first MAX_CHARS...
        
        with open(target_dir, "r") as f:
            what_read = f.read(MAX_CHARS)
            if f.read(1):
                what_read += f'[...File "{file_path}" truncated at {MAX_CHARS} characters]'
            
        return what_read
        
    
    except Exception as e:
        return f"Error: type={type(e).__name__}, message: {e}"
    



schema_get_file_content = types.FunctionDeclaration(
    name="get_file_content",
    description="Lists the content of a file at a given directory and file path.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The path to the file.  Must be inside the working directory.  Must be a file and not a directory.",
            ),
        },
        required=["file_path"],
    ),
)