def common_elements():
    mult3 = [x for x in range(100) if x % 3 == 0]
    mult5 = [x for x in range(100) if x % 5 == 0]
    return set(mult3) & set(mult5)


assert common_elements() == {0, 75, 45, 15, 90, 60, 30}

print('OK')