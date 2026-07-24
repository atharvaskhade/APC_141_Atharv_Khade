status = input("Enter marriatial staus(Y/N)")
gender = input("Enter Gender(M/F)")
age = int(input("Enter age"))

if(status == 'Y' or status == 'y'):
    print("Driver is insured")
elif((status == 'N' or status == 'n')and age>25 and (gender=='F'or gender == 'f')):
    print("Driver is insured")
elif((status == 'N' or status == 'n')and age>30 and (gender=='M'or gender == 'm')):
    print("Driver is insured")
else:
    print("Driver is not insured ")
