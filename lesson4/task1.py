list1 = [0, 1, 7, 2, 4, 8]
list2 = [1, 3, 5]
list3 = [6]
list4 = []

def changelist(lst : list) -> int:
    if len(lst) == 0:
        return 0

    return sum([x for i, x in enumerate(lst) if i % 2 == 0]) * lst[-1]

print(changelist(list1))
print(changelist(list2))
print(changelist(list3))
print(changelist(list4))