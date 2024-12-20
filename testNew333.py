def second_number(list):
    max = 0
    for i in list:
        if i > max:
            max = i
    list.remove(max)
    max2 = 0
    for i in list:
        if i > max2:
            max2 = i
    print(max2)

name = [3,2,6,9,1]
second_number(name)

