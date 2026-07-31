# Program to check whether two strings are anagrams

str1 = input("Enter first string: ")
str2 = input("Enter second string: ")

# Remove spaces and convert to lowercase
str1 = str1.replace(" ", "").lower()
str2 = str2.replace(" ", "").lower()

if len(str1) != len(str2):
    print("The strings are not Anagrams.")
else:
    is_anagram = True

    for ch in str1:
        if str1.count(ch) != str2.count(ch):
            is_anagram = False
            break

    if is_anagram:
        print("The strings are Anagrams.")
    else:
        print("The strings are not Anagrams.")