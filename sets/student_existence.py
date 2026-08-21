# Create a set of student names
students = {"Alice", "Bob", "Charlie", "David", "Emma"}

# Ask the user to enter a name
search_name = input("Enter a student's name to check: ")

# Check whether the student exists in the set
if search_name in students:
    print(f"Yes, {search_name} exists in the set.")
else:
    print(f"No, {search_name} does not exist in the set.")
