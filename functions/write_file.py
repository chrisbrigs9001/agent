import os
from google.genai import types



def write_file(working_directory, file_path, content):
    
    try:
        working_dir_abs = (os.path.abspath(working_directory))
        target_dir = os.path.normpath(os.path.join(working_dir_abs, file_path))
        
        # Will be True or False
        valid_target_dir = os.path.commonpath([working_dir_abs, target_dir]) == working_dir_abs
        
        if not valid_target_dir:
            return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
        
        if os.path.isdir(target_dir):
                return f'Error: Cannot write to "{file_path}" as it is a directory'
        
        os.makedirs(os.path.dirname(target_dir), exist_ok=True)
        
        with open(target_dir, "w") as f:
            f.write(content)
        
        return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
        
        
    except Exception as e:
        return f"Error: type={type(e).__name__}, message: {e}"
    
    

schema_write_file = types.FunctionDeclaration(
    name="write_file",
    description="Writes the content to a file at the given file_path.  Will only write if the file_path points to a file, not a directory. If the file does not exist, it will be created. Returns the lenght of characters written to the file with the success message.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The path to the file to be written in.",
            ),
            "content": types.Schema(
                type=types.Type.STRING,
                description="The content that will be written to the file",
            ),
        },
        required=["file_path", "content"],
    ),
)