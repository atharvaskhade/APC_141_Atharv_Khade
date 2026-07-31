# Program to remove duplicate characters while maintaining the original order

text = input("Enter a string: ")

result = ""

for ch in text:
    if ch not in result:
        result += ch

print("String after removing duplicates:", result)