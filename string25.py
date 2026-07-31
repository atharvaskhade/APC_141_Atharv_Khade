# Program to find the second most frequently occurring character

text = input("Enter a string: ")

first_char = ""
second_char = ""
first_count = 0
second_count = 0

checked = ""

for i in range(len(text)):
    if text[i] not in checked:
        count = 0

        for j in range(len(text)):
            if text[i] == text[j]:
                count += 1

        if count > first_count:
            second_count = first_count
            second_char = first_char
            first_count = count
            first_char = text[i]

        elif count > second_count and count != first_count:
            second_count = count
            second_char = text[i]

        checked += text[i]

if second_char == "":
    print("No second most frequent character found.")
else:
    print("Second most frequent character:", second_char)
    print("Frequency:", second_count)