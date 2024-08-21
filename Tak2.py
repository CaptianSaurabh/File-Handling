# Task: Open and read the contents of the file you just created
with open("Task1_file.txt", "r") as file:
    content = file.read()
    print(content)