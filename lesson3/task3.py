my_list = [10, 20, 30, 40, 50, 60, 70]

lenOfList = len(my_list)

if lenOfList % 2 != 0:
    number = lenOfList // 2
    fistList = my_list[:number+1]
    secondList = my_list[number+1:]
    result = [fistList, secondList]
    print("Result", result)
else:
    number = lenOfList // 2
    fistList = my_list[:number]
    secondList = my_list[number:]
    result = [fistList, secondList]
    print("Result", result)