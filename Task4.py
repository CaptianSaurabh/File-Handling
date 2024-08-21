# Task: Read and print each line from the file one by one
# Open the file in read mode
file = open("Task1_file.txt", "r")

# Read and print each line from the file one by one
for line in file:
    print(line)

# Close the file
file.close()