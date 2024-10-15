import os

resources = {"water": 1000,
"milk": 1000,
"coffee": 1000,
"money": 0
}

def verify_resources(item, resources):
    if item < resources:
        return True
    else:
        return False

def check_resources(coffee):
    w = verify_resources(coffee["water"], resources["water"])
    m = verify_resources(coffee["milk"], resources["milk"])
    c = verify_resources(coffee["coffee"], resources["coffee"])
    if w == False:
        return "Water is less"
    elif m == False:
        return "Milk is less"
    elif c == False:
        return "Coffee is less"
    else:
        return True

def coffee_type(latte_required, money, money_required):
    resources["money"] += money
    if money_required == money:
        for i in latte_required:
            resources[i] = resources[i] - latte_required[i]
        return True
    elif money_required < money:
        refund = money - money_required
        resources["money"] -= refund
        print(f"Ohh...extra money provided, please take refund {refund}")
        for i in latte_required:
            resources[i] = resources[i] - latte_required[i]
        return True
    else:
        print(f"Sorry, sufficient payment not done, please take refund {money}")
        return False

def ask_user():
    print("Welcome to the coffee machine !!!!!!!!")
    print("latte: 150, expresso: 200, cappuccino: 300")
    print("Type admin for ADMIN menu")
    choice = input("What would you like to have? (latte/expresso/cappuccino): ")
    coffee_prices = {"latte": 150, "expresso": 200, "cappuccino": 300}
    if choice == 'admin':
        choice = input("Welcome admin: Report or Recharge ? : ")
        money = 0
        money_required = 0
    elif choice == "latte" or choice == "expresso" or choice == "cappuccino":
        money_required = coffee_prices[choice]
        money = int(input(f"Please pay Rs {money_required} : "))
    else:
        choice = ""
        money = 0
        money_required = 0

    return choice, money, money_required

def coffee_processing(choice, money, money_required):
    if choice == "latte":
        latte_required = {"water": 200, "milk": 50, "coffee": 75}
        resource_flag = check_resources(latte_required)
        if resource_flag == True:
            coffee_flag = coffee_type(latte_required, money, money_required)
            if coffee_flag:
                print("Here is your latte !!!")
        else:
            print(resource_flag)
            print(f"please take refund {money}")

    elif choice == "expresso":
        expresso_required = {"water": 150, "milk": 0, "coffee": 200}
        resource_flag = check_resources(expresso_required)
        if resource_flag == True:
            coffee_flag = coffee_type(expresso_required, money, money_required)
            if coffee_flag:
                print("Here is your expresso !!!")
        else:
            print(resource_flag)
            print(f"please take refund {money}")

    elif choice == "cappuccino":
        cappuccino_required = {"water": 100, "milk": 250, "coffee": 100}
        resource_flag = check_resources(cappuccino_required)
        if resource_flag == True:
            coffee_flag = coffee_type(cappuccino_required, money, money_required)
            if coffee_flag:
                print("Here is your cappuccino !!!")
        else:
            print(resource_flag)
            print(f"please take refund {money}")

    elif choice == "report":
        for i in resources:
            print(f"{i} : {resources[i]}")

    elif choice == "recharge":
        print(resources)
        item = int(input("Please enter number to select item for recharge\n "
                       "1: water \n"
                       "2: milk \n"
                       "3: coffee \t :"))
        if item in [1,2,3]:
            recharge = recharge_process(item)
            if recharge:
                print("Recharge is successfull !!!")
        else:
            print("Invalid Input !")
    else:
        print("Invalid Input")

def recharge_process(item):
    value = int(input("Enter value to recharge : "))
    if item == 1:
        resources["water"] = resources["water"] + value
    elif item == 2:
        resources["milk"] = resources["milk"] + value
    elif item == 3:
        resources["coffee"] = resources["coffee"] + value
    else:
        print("Invalid Input")
        return False

    return True

if __name__ == '__main__':
    choice, money, money_required = ask_user()
    coffee_processing(choice, money, money_required)
    flag = True
    while flag == True:
        want_continue = input("Want anything more ? (yes/no): ").lower()
        if want_continue == "yes":
            os.system("cls")
            choice, money, money_required = ask_user()
            coffee_processing(choice, money, money_required)
        elif want_continue == "no":
            flag = False
            os.system("cls")
            print("Thank you")
        else:
            print("Invalid Input !")
            flag = True
