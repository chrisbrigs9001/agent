import os
from google.genai import types


def get_files_info(working_directory, directory="."):
    try:
        working_dir_abs = (os.path.abspath(working_directory))
        target_dir = os.path.normpath(os.path.join(working_dir_abs, directory))
        
        # Will be True or False
        valid_target_dir = os.path.commonpath([working_dir_abs, target_dir]) == working_dir_abs
        
        if not valid_target_dir:
            return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
        
        if not os.path.isdir(target_dir):
            return f'Error: "{directory}" is not a directory'
        
        my_list = []
        for item in os.listdir(target_dir):
            target_target = os.path.join(target_dir, item)
            t_name = item
            t_file_size = os.path.getsize(target_target)
            t_is_dir = os.path.isdir(target_target)
            my_list.append(f"- {t_name}: file_size={t_file_size} bytes, is_dir={t_is_dir}")
        
        return '\n'.join(my_list)
    
    except Exception as e:
        return f"Error: type={type(e).__name__}, message: {e}"
    
    



schema_get_files_info = types.FunctionDeclaration(
    name="get_files_info",
    description="Lists files in a specified directory relative to the working directory, providing file size and directory status",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "directory": types.Schema(
                type=types.Type.STRING,
                description="Directory path to list files from, relative to the working directory (default is the working directory itself)",
            ),
        },
    ),
)