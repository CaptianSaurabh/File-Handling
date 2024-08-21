# Read the file content into a list, where each line is an element of the list

# Open the file in read mode
with open("Task5_fruits.txt", "r") as file:
    # Read the file content into a list, where each line is an element of the list
    my_list = [line.strip() for line in file]

print(my_list)