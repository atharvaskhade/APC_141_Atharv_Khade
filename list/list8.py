# Store 15 integers in a list

numbers = [12, 7, 25, 18, 9, 30, 41, 56, 63, 84, 15, 22, 11, 48, 50]

even_count = 0
odd_count = 0

# Count even and odd numbers
for num in numbers:
    if num % 2 == 0:
        even_count += 1
    else:
        odd_count += 1

# Display the results
print("List:", numbers)
print("Even numbers:", even_count)
print("Odd numbers:", odd_count)