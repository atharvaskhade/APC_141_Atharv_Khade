# Sets representing products belonging to different categories
electronics = {"Laptop", "Phone", "Smartwatch", "Charger"}
office_supplies = {"Notebook", "Pen", "Laptop", "Charger"}

# Find products that belong to both categories
both_categories = electronics.intersection(office_supplies)

# Display results
print("Electronics products:", electronics)
print("Office Supplies products:", office_supplies)
print("Products belonging to both categories:", both_categories)
