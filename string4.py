

text = input("Enter a string: ")

reverse = ""

for ch in text:
    reverse = ch + reverse

if text == reverse:
    print("The string is a Palindrome.")
else:
    print("The string is not a Palindrome.")