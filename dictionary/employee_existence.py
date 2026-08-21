# Create a dictionary of employee IDs and names
employees = {
    "E101": "Amit",
    "E102": "Bina",
    "E103": "Chirag",
    "E104": "Divya"
}

# Ask the user for an employee ID
search_id = input("Enter Employee ID to search: ")

# Check whether it exists
if search_id in employees:
    print(f"Employee found: {employees[search_id]}")
else:
    print("Employee ID does not exist.")
