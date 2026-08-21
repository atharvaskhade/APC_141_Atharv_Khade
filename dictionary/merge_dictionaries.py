# Create two dictionaries
dict_a = {"apple": 5, "banana": 3}
dict_b = {"cherry": 7, "date": 2}

# Merge them into a single dictionary
merged_dict = dict_a.copy()
merged_dict.update(dict_b)

# Display results
print("Dictionary A:", dict_a)
print("Dictionary B:", dict_b)
print("Merged Dictionary:", merged_dict)
