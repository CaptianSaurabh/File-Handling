#  Task: Add additional text to the existing file without deleting the current content
# Open the file in append mode
file = open("Task1_file.txt", "a")

# Add additional text to the file
file.write("This is the fourth line of text.\n")
file.write("This is the fifth line of text.\n")

# Close the file
file.close()