# Read a file line by line

with open("student.txt", "r") as file:
    for line in file:
        print(line, end="")