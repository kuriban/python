length = input("Введіть довжину: ")
height = input("Введіть ширину: ")

try:
    length = int(length)

    try:
        height = int(height)
        print("Периметр:", length*2 + height*2)
    except ValueError:
        print("Please enter a number of height")
except ValueError:
    print("Please enter a number of length")



