# Program to count the occurrences of a specific word in a sentence

sentence = input("Enter a sentence: ")
search_word = input("Enter the word to search: ")

word = ""
count = 0

for ch in sentence + " ":
    if ch != " ":
        word += ch
    else:
        if word == search_word:
            count += 1
        word = ""

print("The word", search_word, "appears", count, "times.")