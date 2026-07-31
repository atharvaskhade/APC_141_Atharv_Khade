# Program to display the frequency of every character in a string

text = input("Enter a string: ")

checked = ""

for i in range(len(text)):
    if text[i] not in checked:
        count = 0

        for j in range(len(text)):
            if text[i] == text[j]:
                count += 1

        print(text[i], ":", count)
        checked += text[i]