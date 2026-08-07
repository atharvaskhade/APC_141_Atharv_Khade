# Program to reverse a list without using reverse()

numbers = [10, 20, 30, 40, 50]

reversed_list = []

# Reverse the list
for i in range(len(numbers) - 1, -1, -1):
    reversed_list.append(numbers[i])

# Display the original and reversed lists
print("Original List:", numbers)
print("Reversed List:", reversed_list)