# Program to check whether a substring exists in the main string

main_string = input("Enter the main string: ")
substring = input("Enter the substring: ")

found = False

for i in range(len(main_string) - len(substring) + 1):
    match = True

    for j in range(len(substring)):
        if main_string[i + j] != substring[j]:
            match = False
            break

    if match:
        found = True
        break

if found:
    print("Substring exists in the main string.")
else:
    print("Substring does not exist in the main string.")