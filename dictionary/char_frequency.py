# Accept a string from the user
user_string = input("Enter a string: ")

# Create a dictionary containing each character and its frequency
frequency = {}
for char in user_string:
    frequency[char] = frequency.get(char, 0) + 1

# Display the dictionary
print("Character frequencies:", frequency)
