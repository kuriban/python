value = input("Enter a number: ")

try:
    value = int(value)
    value = str(value)
    print(value[len(value) - 1])
except ValueError:
    print("Please enter a number")