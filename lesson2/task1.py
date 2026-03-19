value = input("Enter a number: ")

try:
    result = int(value) ** 2
    print("Квадрат числа:", result)
except ValueError:
    print("Please enter a number")