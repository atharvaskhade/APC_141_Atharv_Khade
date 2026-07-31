# Program to find the shortest word in a sentence

sentence = input("Enter a sentence: ")

word = ""
shortest = ""

for ch in sentence:
    if ch != " ":
        word += ch
    else:
        if word != "":
            if shortest == "" or len(word) < len(shortest):
                shortest = word
        word = ""

# Check the last word
if word != "":
    if shortest == "" or len(word) < len(shortest):
        shortest = word

print("Shortest word:", shortest)
print("Length:", len(shortest))