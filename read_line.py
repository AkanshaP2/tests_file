# file path
file_path = “/content/python_files/test.txt”

with open(file_path, 'r') as file:
    # Read the first line of the file
    first_line = file.readline()
    print("First line of the file using readline():", first_line)

    # Read the second line
    second_line = file.readline()
    print("Second line of the file using readline():", second_line)
