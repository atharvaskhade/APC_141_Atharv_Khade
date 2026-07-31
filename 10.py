n = int(input("Enter number: "))

i = 2
prime = True

if n < 2:
    prime = False

while i < n:
    if n % i == 0:
        prime = False
        break
    i += 1

if prime:
    print("Prime")
else:
    print("Not Prime")