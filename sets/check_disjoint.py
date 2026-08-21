# Create two sets
set_a = {1, 2, 3}
set_b = {4, 5, 6}

# Determine whether the two sets have no elements in common (disjoint)
no_common_elements = set_a.isdisjoint(set_b)

# Display the results
print("Set A:", set_a)
print("Set B:", set_b)
print("Do the sets have no elements in common?", no_common_elements)
