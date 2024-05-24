file_path =  “/content/python_files/test.txt”

lines_to_write = [
    "writing a line.\n",
    "writing another line.\n",
    "Writing one more line.\n"
]

with open(file_path, 'w') as file:
    # Write the list of lines to the file
    file.writelines(lines_to_write)

print(f"Content successfully written to '{file_path}'")
