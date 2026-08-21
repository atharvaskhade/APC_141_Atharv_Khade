# Create a dictionary containing duplicate values
original_dict = {
    "a": 1,
    "b": 2,
    "c": 1,
    "d": 3,
    "e": 2
}
print("Original dictionary:", original_dict)

# Remove duplicate values while keeping the first occurrence
unique_dict = {}
seen_values = set()
for key, val in original_dict.items():
    if val not in seen_values:
        unique_dict[key] = val
        seen_values.add(val)

# Display result
print("Dictionary after removing duplicate values:", unique_dict)
