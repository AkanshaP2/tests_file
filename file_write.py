import os

# file path
file_path = “/content/python_files/test.txt”

with open(file_path, 'w') as file:
    # Writing content to the file
    file.write("This is a line written to the file.")

print(f"Content successfully written to '{file_path}'")
