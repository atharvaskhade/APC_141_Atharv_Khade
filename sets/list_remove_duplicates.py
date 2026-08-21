# Create a list containing duplicate numbers
numbers_list = [1, 2, 2, 3, 4, 4, 4, 5, 5, 6]
print("Original list:", numbers_list)

# Use a set to remove the duplicates and convert back to list
unique_list = list(set(numbers_list))

# Display the unique list
print("List after removing duplicates:", unique_list)
