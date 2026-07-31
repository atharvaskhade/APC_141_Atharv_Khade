n = int(input("How many numbers? "))

i = 1
largest = None

while i <= n:
    num = int(input("Enter number: "))
    if largest is None or num > largest:
        largest = num
    i += 1

print("Largest =", largest)