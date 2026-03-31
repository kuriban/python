import sys

def calculator(first_number, second_number, action):
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

repeat = False

while not repeat:
    first = int(input("Enter first number:"))
    second = int(input("Enter second number:"))

    act = input("Enter a action * / - +: ")

    calculator(first, second, act)

    repeat_question = input("Would you like to repeat ? yes/n: ")
    repeat = repeat_question.lower()[0] != 'y'
