# Input string
text = "swiss"
print("Input string:", text)

# Count character frequencies using a dictionary
char_counts = {}
for char in text:
    char_counts[char] = char_counts.get(char, 0) + 1

# Find the first character with a frequency of 1
first_unique = None
for char in text:
    if char_counts[char] == 1:
        first_unique = char
        break

# Display result
if first_unique:
    print(f"The first character that occurs only once is: '{first_unique}'")
else:
    print("There are no unique characters in the string.")
