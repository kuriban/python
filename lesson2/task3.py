value = input("Введіть кількість хвилин: ")

try:
    value = int(value)
    hours = value // 60
    minutes = value - hours*60
    print("hours", hours, ":", "minutes", minutes)
except ValueError:
    print("Please enter a number")