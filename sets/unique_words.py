# Accept a sentence from the user
sentence = input("Enter a sentence: ")

# Split the sentence into words and convert them to lowercase
words = sentence.lower().split()

# Use a set to display all unique words
unique_words = set(words)

# Display the unique words
print("Unique words in the sentence:", unique_words)
