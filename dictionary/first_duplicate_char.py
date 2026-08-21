# Input string
text = "swiss"
print("Input string:", text)

# Count character frequencies using a dictionary
char_counts = {}
for char in text:
    char_counts[char] = char_counts.get(char, 0) + 1

# Find the first character with a frequency greater than 1
first_duplicate = None
for char in text:
    if char_counts[char] > 1:
        first_duplicate = char
        break

# Display result
if first_duplicate:
    print(f"The first character that occurs more than once is: '{first_duplicate}'")
else:
    print("There are no duplicate characters in the string.")
