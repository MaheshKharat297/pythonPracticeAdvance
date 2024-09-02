def searchNum(lst, num):
    status = False
    if num in lst:
        status = True
    else:
        print(f"The {num} is not present in the list")

    while status:
        for i in lst:
            if i == num:
                ind = lst.index(i)
                print(f"The {num} is present in list at {ind} position")
                status = False

lst = [3,45,9,32,100,43]
n = 3
searchNum(lst, n)
