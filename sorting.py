def sorting(lst):
    dict1 = {}
    for i in lst:
        x = len(i)
        dict1[i] = x

    values = list(dict1.values())
    values.sort()
    lst_final = []
    for i in values:
        for j in dict1:
            if i == dict1[j] and j not in lst_final :
                lst_final.append(j)

    print(lst_final)

def length(lst):
    return len(lst)

lst = ["pune","goa","mumbai","nagpur","sambhajinagar"]
sort = sorted(lst, key=length)
print(sort)
sorting(lst)
