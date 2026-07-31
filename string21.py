# Program to validate a password

password = input("Enter a password: ")

uppercase = False
lowercase = False
digit = False
special = False

special_chars = "!@#$%^&*()-_=+[]{}|\\:;\"'<>,.?/`~"

for ch in password:
    if ch.isupper():
        uppercase = True
    elif ch.islower():
        lowercase = True
    elif ch.isdigit():
        digit = True
    elif ch in special_chars:
        special = True

if (len(password) >= 8 and uppercase and lowercase and digit and special):
    print("Password is Valid.")
else:
    print("Password is Invalid.")
    print("Password must contain:")
    print("- Minimum 8 characters")
    print("- At least one uppercase letter")
    print("- At least one lowercase letter")
    print("- At least one digit")
    print("- At least one special character")