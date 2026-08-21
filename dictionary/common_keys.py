# Given two dictionaries
dict_a = {"apple": 5, "banana": 3, "cherry": 7}
dict_b = {"banana": 8, "cherry": 10, "date": 2}

# Find common keys using set intersection of keys
common_keys = set(dict_a.keys()).intersection(set(dict_b.keys()))

# Display results
print("Dict A:", dict_a)
print("Dict B:", dict_b)
print("Common keys:", common_keys)
