# Create a dictionary containing student names and marks
student_marks = {
    "Alice": 85,
    "Bob": 78,
    "Charlie": 92,
    "David": 64,
    "Emma": 88
}

# Find the student who has scored the lowest marks
lowest_student = min(student_marks, key=student_marks.get)
lowest_score = student_marks[lowest_student]

# Display the results
print("Student marks:", student_marks)
print(f"Student with lowest marks: {lowest_student} ({lowest_score})")
