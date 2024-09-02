def addNumbers(num):
    sum = 0
    for i in num:
        n = int(i)
        sum += n
    print(f"The sum of digits is : {sum}")

num = input("Enter any number : ")
addNumbers(num)