from random import randint

def changelist():
    count = randint(3, 10)

    lst = [randint(1, 10) for _ in range(count)]
    # print(lst, "===", [x for i, x in enumerate(lst) if i == 0 or i == 2 or i == len(lst) - 2])
    return (lst, "===", [lst[0], lst[2], lst[-2]])

print(changelist())
print(changelist())
print(changelist())
