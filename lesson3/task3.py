my_list = []

lenOfList = len(my_list)

if lenOfList == 0:
    result = [[], []]
elif lenOfList % 2 != 0:
    number = lenOfList // 2
    fistList = my_list[:number+1]
    secondList = my_list[number+1:]
    result = [fistList, secondList]
else:
    number = lenOfList // 2
    fistList = my_list[:number]
    secondList = my_list[number:]
    result = [fistList, secondList]

print("Result", result)