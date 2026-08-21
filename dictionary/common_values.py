# Given two dictionaries
dict_a = {"apple": 5, "banana": 3, "cherry": 7}
dict_b = {"pear": 3, "grape": 7, "orange": 9}

# Identify the values that are common to both dictionaries
common_values = set(dict_a.values()).intersection(set(dict_b.values()))

# Display results
print("Dict A:", dict_a)
print("Dict B:", dict_b)
print("Common values:", common_values)
