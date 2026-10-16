# Open a text file and display its contents

with open("student.txt", "r") as file:
    content = file.read()
    print(content)