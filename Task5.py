# Task: Write the contents of a list to a file, with each item on a new line
# Create a list
my_list = ["apple", "banana", "cherry", "date", "elderberry"]

# Open the file in write mode
with open("Task5_fruits.txt", "w") as file:
    # Write each item from the list to the file, with each item on a new line
    for item in my_list:
        file.write(item + "\n")