def split(str):
    str1 = []
    str2 = []
    str3 = []
    mid = len(str)//2
    print(mid)
    count = 0
    for i in str:
        if count < mid:
            str1.append(i)
            count += 1
        elif count == mid:
            str2.append(i)
            count += 1
        elif count > mid:
            str3.append(i)
            count += 1
        else:
            break
    str_first = ''.join(str1)
    str_sec = ''.join(str2)
    str_third = ''.join(str3)

    final_str = str_third + str_sec + str_first
    print(final_str)

str = "maheshdkharat"
split(str)