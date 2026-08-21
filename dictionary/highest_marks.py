# Create a dictionary containing student names and marks
student_marks = {
    "Alice": 85,
    "Bob": 78,
    "Charlie": 92,
    "David": 64,
    "Emma": 88
}

# Find the student who has scored the highest marks
highest_student = max(student_marks, key=student_marks.get)
highest_score = student_marks[highest_student]

# Display the results
print("Student marks:", student_marks)
print(f"Student with highest marks: {highest_student} ({highest_score})")
