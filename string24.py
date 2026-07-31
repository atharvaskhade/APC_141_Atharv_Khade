# Program to find the character with the highest frequency

text = input("Enter a string: ")

max_char = ""
max_count = 0
checked = ""

for i in range(len(text)):
    if text[i] not in checked:
        count = 0

        for j in range(len(text)):
            if text[i] == text[j]:
                count += 1

        if count > max_count:
            max_count = count
            max_char = text[i]

        checked += text[i]

print("Character with highest frequency:", max_char)
print("Frequency:", max_count)