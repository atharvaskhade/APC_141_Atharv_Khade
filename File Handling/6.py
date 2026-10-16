# Count the total number of words in a file

with open("student.txt", "r") as file:
    content = file.read()
    words = content.split()
    print("Total number of words:", len(words))