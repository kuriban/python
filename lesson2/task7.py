value = input("Enter a number: ")

if len(value) != 4:
    print("Please enter a 4-х значне число")
else:
    try:
        value = int(value)
        d1 = value // 1000
        d2 = value % 1000 // 100
        d3 = value % 100 // 10
        d4 = value % 10

        print(d1)
        print(d2)
        print(d3)
        print(d4)
    except ValueError:
        print("Please enter a number")