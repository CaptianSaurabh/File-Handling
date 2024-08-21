# Task: Create a new text file and write a few lines of text into it

# Open a new file in write mode
file = open("Task1_file.txt", "w")

# Write a few lines of text into the file
file.write("This is the first line of text.\n")
file.write("This is the second line of text.\n")
file.write("This is the third line of text.\n")

# Close the file
file.close()