def findPrimNumber(num):
    primNo = []
    for i in range(num):
        count = 0
        for j in range(2, int((i/2)+1)):
            if i % j == 0:
                count += 1
        if count == 0 and i not in primNo:
            primNo.append(i)

    print(primNo)


findPrimNumber(10)