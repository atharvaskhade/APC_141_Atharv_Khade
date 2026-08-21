# Create a dictionary containing student names and marks
students = {"Alice": 85, "Bob": 78, "Charlie": 92}

while True:
    print("\n--- Student Manager ---")
    print("1. Add Student")
    print("2. Update Marks")
    print("3. Delete Student")
    print("4. Search Student")
    print("5. Display All Students")
    print("6. Find Highest Marks")
    print("7. Calculate Average")
    print("8. Exit")
    
    choice = input("Enter choice (1-8): ")
    
    if choice == '1':
        name = input("Enter name: ")
        marks = float(input("Enter marks: "))
        students[name] = marks
        print("Student added successfully.")
    elif choice == '2':
        name = input("Enter student name: ")
        if name in students:
            marks = float(input("Enter new marks: "))
            students[name] = marks
            print("Marks updated.")
        else:
            print("Student not found.")
    elif choice == '3':
        name = input("Enter student name to delete: ")
        if name in students:
            students.pop(name)
            print("Student deleted.")
        else:
            print("Student not found.")
    elif choice == '4':
        name = input("Enter student name to search: ")
        if name in students:
            print(f"{name} scored {students[name]} marks.")
        else:
            print("Student not found.")
    elif choice == '5':
        print("\nAll Students:")
        for k, v in students.items():
            print(f"{k}: {v}")
    elif choice == '6':
        if students:
            highest_student = max(students, key=students.get)
            print(f"Highest Marks: {highest_student} ({students[highest_student]})")
        else:
            print("No students in records.")
    elif choice == '7':
        if students:
            avg = sum(students.values()) / len(students)
            print(f"Average Marks: {avg:.2f}")
        else:
            print("No students in records.")
    elif choice == '8':
        print("Goodbye!")
        break
    else:
        print("Invalid choice.")
