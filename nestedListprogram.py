def nestedList(lst, num, x, y):
    x = x-1
    y = y-1
    print("Current value is : ", lst[x][y])
    lst[x][y] = num
    return lst


lst = [[1,1,1],[1,1,1],[1,1,1]]
num = int(input("Please enter the Number to append in List : "))
x = int(input("Enter X value : "))
y = int(input("Enter Y value : "))

final = nestedList(lst, num, x, y)
print(f"Updated list is : {final} ")