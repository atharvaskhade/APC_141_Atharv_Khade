# Program to find the longest word in a sentence

sentence = input("Enter a sentence: ")

word = ""
longest = ""

for ch in sentence:
    if ch != " ":
        word += ch
    else:
        if len(word) > len(longest):
            longest = word
        word = ""

# Check the last word
if len(word) > len(longest):
    longest = word

print("Longest word:", longest)
print("Length:", len(longest))