# Create a dictionary containing employee names and salaries
salaries = {
    "Amit": 45000,
    "Bina": 65000,
    "Chirag": 52000,
    "Divya": 48000,
    "Emma": 70000
}

# Find highest, lowest, average salary
highest = max(salaries.values())
lowest = min(salaries.values())
average = sum(salaries.values()) / len(salaries)

# Employees earning more than 50,000
high_earners = []
for emp, sal in salaries.items():
    if sal > 50000:
        high_earners.append(emp)

# Display results
print("Employee Salaries:", salaries)
print(f"Highest Salary: Rs. {highest}")
print(f"Lowest Salary: Rs. {lowest}")
print(f"Average Salary: Rs. {average:.2f}")
print("Employees earning more than Rs. 50,000:", high_earners)
