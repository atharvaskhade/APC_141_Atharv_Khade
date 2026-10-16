# Count the total number of lines in a file

with open("student.txt", "r") as file:
    lines = file.readlines()
    print("Total number of lines:", len(lines))