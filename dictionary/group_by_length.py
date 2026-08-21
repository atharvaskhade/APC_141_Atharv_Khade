# List of words
words_list = ["apple", "banana", "cat", "dog", "cherry", "fig"]
print("Original word list:", words_list)

# Create a dictionary where key = length, value = list of words
grouped_by_len = {}
for word in words_list:
    length = len(word)
    if length not in grouped_by_len:
        grouped_by_len[length] = []
    grouped_by_len[length].append(word)

# Display results
print("Words grouped by length:", grouped_by_len)
