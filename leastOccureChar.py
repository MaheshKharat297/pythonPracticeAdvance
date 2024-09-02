def least_achr(str):
    count_dict = {}
    str1 = list(set(str))
    #print(str1)
    for i in str1:
        count = 0
        for j in str:
            if i == j:
                count += 1
        count_dict[i] = count
    print(count_dict)
    mi = min(count_dict.values())
    key = list(count_dict.keys())
    least = []
    for i in key:
        if count_dict[i] == mi:
            least.append(i)

    print("Least value keys are :", least)

str="thisistestem"
least_achr(str)