# Sets representing students enrolled in courses
python_students = {"Alice", "Bob", "Charlie", "David"}
java_students = {"Charlie", "David", "Emma", "Frank"}

# Find students enrolled in both courses
both_courses = python_students.intersection(java_students)

# Find students enrolled in only one course (symmetric difference)
only_one_course = python_students.symmetric_difference(java_students)

# Display results
print("Students enrolled in both Python and Java:", both_courses)
print("Students enrolled in only one course:", only_one_course)
