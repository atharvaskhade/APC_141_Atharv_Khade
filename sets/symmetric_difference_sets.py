# Create two sets of numbers
set_a = {1, 2, 3, 4}
set_b = {3, 4, 5, 6}

# Find the elements present in either set but not in both (symmetric difference)
sym_diff = set_a.symmetric_difference(set_b)

# Display the results
print("Set A:", set_a)
print("Set B:", set_b)
print("Elements present in either set but not both:", sym_diff)
