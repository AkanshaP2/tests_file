file_path =c

with open(file_path, 'r') as file:
    # read all lines into a list
    lines = file.readlines()
    
    # show each line
    print("File content using readlines():")
    for line in lines:
        print(line.strip()) 
