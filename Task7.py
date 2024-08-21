# Task: Write the contents of a list to a file, with each item on a new line
# Open the file in read mode
with open("Task5_fruits.txt", "r") as file:
    # Read the file content
    content = file.read()

# Split the content into words and count the total number of words
total_words = len(content.split())

print("Total number of words:", total_words)