# Task: Delete a file using Python
import os

def delete_file(file_path):
    try:
        os.remove(file_path)
        print(f"The file {file_path} has been deleted.")
    except FileNotFoundError:
        print(f"The file {file_path} does not exist.")
    except PermissionError:
        print(f"Permission denied to delete the file {file_path}.")
    except OSError as e:
        print(f"Error deleting the file {file_path}: {e.strerror}")

file_path = "D:\File handling\File_Path.txt"
delete_file(file_path)