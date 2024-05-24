import os

# filepath
file_path = “/content/python_files/test.txt”

if os.path.exists(file_path):
    with open(file_path, 'r') as file:
        # Read file contents
        content = file.read()
        print("File content:\n", content)
else:
    print(f"File '{file_path}' not found.")
