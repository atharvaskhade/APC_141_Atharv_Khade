# List of integers and target value
numbers = [2, 7, 11, 15]
target = 9
print("List of numbers:", numbers)
print("Target sum:", target)

# Find two numbers whose sum is equal to target using a dictionary
seen = {}
found = False
for num in numbers:
    complement = target - num
    if complement in seen:
        print(f"Numbers found: {complement} and {num} (Sum = {target})")
        found = True
        break
    seen[num] = True

if not found:
    print("No two numbers sum up to the target.")
