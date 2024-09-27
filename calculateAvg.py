def cal_Avg(lst):
    sum = 0   #float('-inf')
    count = 0
    for i in lst:
        sum = sum + i
        count += 1

    avg = sum / count
    return avg

num = int(input("Enter the length of list : "))
lst = []
for i in range(num):
    lst_num = int(input("Enter number :"))
    lst.append(lst_num)
print("Entered number list is :", lst)

avg = cal_Avg(lst)
print("The average of the entered numbers is :", avg)