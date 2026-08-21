# Create a dictionary containing student names and marks
student_marks = {
    "Alice": 85,
    "Bob": 78,
    "Charlie": 92,
    "David": 64,
    "Emma": 88
}

# Calculate the average marks of all students
total_marks = sum(student_marks.values())
num_students = len(student_marks)
average = total_marks / num_students

# Display results
print("Student marks:", student_marks)
print(f"Average marks: {average:.2f}")
