# Program to compress a string and return the original if compression is not shorter

text = input("Enter a string: ")

compressed = ""
count = 1

for i in range(len(text)):
    if i < len(text) - 1 and text[i] == text[i + 1]:
        count += 1
    else:
        compressed += text[i] + str(count)
        count = 1

if len(compressed) < len(text):
    print("Compressed string:", compressed)
else:
    print("Original string:", text)