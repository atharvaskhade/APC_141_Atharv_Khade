with open("student.txt", "r") as f:
    words = f.read().split()

if words:
    longest = max(words, key=len)
    print("Longest word:", longest)
    print("Length:", len(longest))
else:
    print("File is empty")