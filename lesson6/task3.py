def multiply_digits(n):
    while n > 9:
        result = 1
        for digit in str(n):
            result *= int(digit)
        n = result
    return n

n = int(input("Введіть число: "))
print(multiply_digits(n))