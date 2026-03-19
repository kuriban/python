price = input("Введіть ціну: ")
discount = input("Введіть знижку (%): ")

try:
    price = int(price)
except ValueError:
    print("Please enter a number of price")

try:
    discount = int(discount)
except ValueError:
    print("Please enter a number of discount")

discountPrice = (price * discount) / 100
print("Ціна зі знижкою: ", price - discountPrice)