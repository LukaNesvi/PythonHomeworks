print("Calculator Prototype")



input1 = input("NUMBER 1: ")
input2 = input("NUMBER 2: ")

numbers = "1234567890"

for c in input1:
    if c not in numbers:
        print("Inncorrect input")
        break

for c in input2:
    if c not in numbers:
        print("Inncorrect input")
        break

input1 = int(input1)
input2 = int(input2)

print ("Actions:| + | - | * | / | ** |")
action = input("What action would you like?: ")

if action == "+":
    print(f"{input1} + {input2} = {input1 + input2}")
elif action == "-":
    print(f"{input1} - {input2} = {input1 - input2}")
elif action == "*":
    print(f"{input1} * {input2} = {input1 * input2}")
elif action == "/":
    print(f"{input1} / {input2} = {input1 / input2}")
elif  action ==  "**":
    print(f"{input1} ^ {input2} = {input1 ** input2}")
else:
    print("Invalid input")