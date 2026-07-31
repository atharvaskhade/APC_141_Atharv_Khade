# Program to print all duplicate characters in a string

text = input("Enter a string: ")

printed = ""

for i in range(len(text)):
    count = 0

    for j in range(len(text)):
        if text[i] == text[j]:
            count += 1

    if count > 1 and text[i] not in printed:
        print(text[i])
        printed += text[i]