def evenSum(num):
    sum = 0
    for i in range(num):
        if i % 2 == 0:
            sum += i
    return sum

def oddSum(num):
    sum = 0
    for i in range(num):
        if i % 2 != 0:
            sum += i
    return sum

num = int(input("Enter any number to range for summation : "))
#sum_even = evenSum(num)

print("Sum of all even numbers is :", evenSum(num))
print("Sum of all odd numbers is : ", oddSum(num))
