# Accept a paragraph from the user
paragraph = input("Enter a paragraph: ")

# Split into words
words = paragraph.split()

# Count the frequency of word lengths
length_counts = {}
for word in words:
    # Clean the word to remove basic punctuation
    cleaned_word = word.strip(".,!?\"'()[]{}")
    if cleaned_word:
        length = len(cleaned_word)
        length_counts[length] = length_counts.get(length, 0) + 1

# Display results
print("\nWord length frequencies:")
for length in sorted(length_counts.keys()):
    print(f"Length {length}: {length_counts[length]} word(s)")
