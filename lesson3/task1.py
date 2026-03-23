import sys

first_number = int(input("Enter first number:"))
second_number = int(input("Enter second number:"))

action = input("Enter a action * / - +: ")

if action == "+":
    print("Result", first_number + second_number)
elif action == "-":
    print("Result", first_number - second_number)
elif action == "*":
    print("Result", first_number * second_number)
elif action == "/":
    if second_number == 0:
        print("Don't allow to divide by zero")
        sys.exit(1)

    print("Result", first_number / second_number)
else:
    print("Unknown action")