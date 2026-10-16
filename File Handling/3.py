# Append additional student information to a file

with open("student.txt", "a") as file:
    file.write("\nAge: 20\n")
    file.write("City: Kolhapur\n")

print("Additional information added successfully!")