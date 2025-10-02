age = int(input("Input your age: "))

if age >= 18:
    status1 = "User is an ADULT"
elif age < 18:
    status1 = "User is a MINOR"
else:
    status1 = "UNDEFINED"

if age % 2 == 0:
    status2 = "User's age is an even number"
elif age % 2 == 1:
    status2 = "User's age is an odd number"
else:
    status2 = "UNDEFINED"

print (f"{status1} \n{status2}")