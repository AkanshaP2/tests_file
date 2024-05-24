try:
    file_path =  “/home/deepcept/python/playground/exception_handle/file_not_present.txt”

    with open(file_path, 'r') as file:
        content = file.read()
    print(f"Content successfully read from '{file_path}'")

except FileNotFoundError:
    print(f"Error: The specified file path '{file_path}' was not found.")
except PermissionError:
    print(f"Error: Permission denied to write to the file '{file_path}'.")
except Exception as e:
    print(f"An unexpected error occurred: {str(e)}")
