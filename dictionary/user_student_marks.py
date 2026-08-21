# Create an empty dictionary
student_marks = {}

# Accept five student names and marks from the user
print("Enter details for 5 students:")
for i in range(1, 6):
    name = input(f"Enter name of student {i}: ")
    marks = float(input(f"Enter marks of student {i}: "))
    student_marks[name] = marks

# Display the dictionary
print("\nStored Student Marks:", student_marks)
