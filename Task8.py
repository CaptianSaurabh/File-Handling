# Open the source file in read mode and the destination file in write mode

with open("Task5_fruits.txt", "r") as source_file, open("Task8_file.txt", "w") as destination_file:
    # Read the content of the source file
    content = source_file.read()

    # Write the content to the destination file
    destination_file.write(content)

print("Contents copied successfully!")