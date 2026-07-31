# Program to convert the first letter of every word to uppercase

sentence = input("Enter a sentence: ")

result = ""
new_word = True

for ch in sentence:
    if new_word and ch.isalpha():
        result += ch.upper()
        new_word = False
    else:
        result += ch
        if ch == " ":
            new_word = True

print("Modified sentence:", result)