from functions.get_file_content import get_file_content

print(f"Result for lorem.txt:\n{(get_file_content('calculator', 'lorem.txt'))}")
print(f"\nResult for main.py:\n{(get_file_content('calculator', 'main.py'))}")
print(f"\nResult for 'pkg/calculatory.py' directory:\n{(get_file_content('calculator', 'pkg/calculator.py'))}")
print(f"\nResult for '/bin/cat' directory:\n{(get_file_content('calculator', '/bin/cat'))}")
print(f"\nResult for 'pkg/does_not_exist.py' directory:\n{(get_file_content('calculator', 'pkg/does_not_exist.py'))}")