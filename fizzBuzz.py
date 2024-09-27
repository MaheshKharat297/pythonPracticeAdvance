def number_print(num):
    for i in range(num+1):
        if i % 3 == 0 and i % 5 == 0:
            print("FIZZ-BUZZ")
        elif i % 5 == 0:
            print("BUZZ")
        elif i % 3 == 0:
            print("FIZZ")
        else:
            print(i)

num = int(input("Enter the number range to print : "))
number_print(num)

