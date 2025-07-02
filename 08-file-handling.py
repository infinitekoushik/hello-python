# File read/write in Python

# Writing to a file
with open("notes.txt", "w") as file:
    file.write("This is my first file.\n")
    file.write("I’m learning Python file handling.")

# Reading the file
with open("notes.txt", "r") as file:
    content = file.read()
    print("File content:\n", content)
