def test(dic):
    keys = list(dic.keys())
    values = list(dic.values())
    values.sort()
    # print(values)
    lst_final = []
    for i in values:
        for j in keys:
            if i == dic[j]:
                lst_final.append(j)

    print(lst_final)


dic = {"A": 2, "B": 1, "C": 0, "D": 4}
test(dic)