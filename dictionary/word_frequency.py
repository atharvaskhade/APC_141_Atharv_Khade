# Accept a sentence from the user
sentence = input("Enter a sentence: ")

# Split into words and convert to lowercase for case-insensitivity
words = sentence.lower().split()

# Create a dictionary containing word frequencies
word_count = {}
for word in words:
    word_count[word] = word_count.get(word, 0) + 1

# Display the dictionary
print("Word frequencies:", word_count)
