def search(lst, n):
    lst.sort()
    l = len(lst)
    u = 0
    print(lst)
    status = False
    if n in lst:
        status = True
    else:
        print(f"The {n} is not present in list")

    while u < l and status == True:
        #print(u, l)
        mid = (u + l) // 2
        #print(mid)
        if lst[mid] == n:
            print(f"The {n} is present in list at {mid}")
            break
        else:
            if lst[mid] < n:
                u = mid
            else:
                l = mid

lst = [3,45,9,32,100,43]
n = 43
search(lst, n)