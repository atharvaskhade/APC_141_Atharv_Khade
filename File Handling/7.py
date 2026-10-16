# Count total characters in a text file, including spaces

with open("student.txt", "r") as file:
    content = file.read()
    print("Total number of characters:", len(content))