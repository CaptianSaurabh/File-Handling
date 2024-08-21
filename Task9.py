# Check if a file exists before attempting to read it

import os

def check_file_exists(file_path):
    if os.path.exists(file_path):
        print(f"The file {file_path} exists.")
        return True
    else:
        print(f"The file {file_path} does not exist.")
        return False

file_path = "D:\File handling\Task8_file.txt"
if check_file_exists(file_path):
    with open(file_path, "r") as file:
        content = file.read()
        print("File content:")
        print(content)
else:
    print("Cannot read the file as it does not exist.")