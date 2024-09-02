def tup_combine(lst):
    uniq_first = []
    for i in lst:
        if i[0] not in uniq_first:
            uniq_first.append(i[0])
    #print(uniq_first)
    final_lst = []
    for i in uniq_first:
        temp_tup = []
        temp_tup.append(i)
        for j in lst:
            if i == j[0]:
                temp_tup.append(j[1])

        final_lst.append(temp_tup)

    print(final_lst)



lst = [(5, 6), (5, 7), (6, 8), (6, 10), (7, 13)]
tup_combine(lst)