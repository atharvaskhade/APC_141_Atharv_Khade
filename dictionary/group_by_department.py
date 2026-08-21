# Student names and their departments
students_dept = {
    "Alice": "Computer Science",
    "Bob": "Electrical",
    "Charlie": "Computer Science",
    "David": "Mechanical",
    "Emma": "Electrical"
}
print("Original dictionary:", students_dept)

# Create a new dictionary that groups students according to department
grouped = {}
for student, dept in students_dept.items():
    if dept not in grouped:
        grouped[dept] = []
    grouped[dept].append(student)

# Display the grouped dictionary
print("Grouped by department:", grouped)
