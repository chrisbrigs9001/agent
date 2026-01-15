from functions.get_files_info import get_files_info

print(f"Result for current directory:\n  {(get_files_info('calculator', '.')).replace('\n', '\n  ')}")
print(f"Result for 'pkg' directory:\n  {(get_files_info('calculator', 'pkg')).replace('\n', '\n  ')}")
print(f"Result for '/bin' directory:\n  {(get_files_info('calculator', '/bin')).replace('\n', '\n  ')}")
print(f"Result for '../' directory:\n  {(get_files_info('calculator', '../')).replace('\n', '\n  ')}")