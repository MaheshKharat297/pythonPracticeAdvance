import os
def calculate(num1, num2, operator):
    if operator == "+":
        result = num1 + num2
    elif operator == "-":
        result = num1 - num2
    elif operator == "*":
        result = num1*num2
    elif operator == "/":
        result = num1/num2
    else:
        print("Invalid Operator !!!")
        result = 0
    return result

if __name__ == '__main__':
    num1 = int(input("Enter First Number : "))
    flag = True
    while flag == True:
        operators = ["*", "+", "-", "/"]
        print(operators)
        operator = input("Select operation with symbol : ")
        num2 = int(input("Enter Next Number : "))

        result = calculate(num1, num2, operator)
        print(f"The result is : {result}")
        print(f'''Enter 'y' to continue calculation with {result} 
                or 
                'n' to start new calculation 
                or 
                'x' to exit ''')
        choice = input("Your choice ? : ").lower()
        if choice == 'y':
            num1 = result
            flag = True
            os.system("cls")
        elif choice == 'n':
            os.system("cls")
            num1 = int(input("Enter First Number : "))
            flag = True
        elif choice == 'x':
            flag = False
            print("Thank you !!")


