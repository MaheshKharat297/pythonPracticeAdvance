def max_number(lst):
    max = float('-inf')
    for i in range(len(lst)):
        if lst[i] > max:
            max = lst[i]

    return max

lst = []
num = int(input("Please enter count of numbers : "))
for i in range(num):
    lst_num = int(input("Enter Number to insert in list : "))
    lst.append(lst_num)

max = max_number(lst)

print("Max number from list is :", max)
