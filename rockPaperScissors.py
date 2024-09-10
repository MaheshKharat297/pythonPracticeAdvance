def result(hand1, hand2):
    if hand1 == "rock" and hand2 == "scissors":
        print(f"Hand 1 having {hand1} is the winner!!")
    elif hand1 == "rock" and hand2 == "paper":
        print(f"Hand 2 having {hand2} is the winner!!")
    elif hand1 == "scissors" and hand2 == "rock":
        print(f"Hand 2 having {hand2} is the winner!!")
    elif hand1 == "scissors" and hand2 == "paper":
        print(f"Hand 1 having {hand1} is the winner!!")
    elif hand1 == "paper" and hand2 == "rock":
        print(f"Hand 1 having {hand1} is the winner!!")
    elif hand1 == "paper" and hand2 == "scissors":
        print(f"Hand 2 having {hand2} is the winner!!")
    else:
        print("Invalid values !!")

def choices(choice):
    if choice == 1:
        return "rock"
    elif choice == 2:
        return "paper"
    elif choice == 3:
        return "scissors"
    else:
        print("Invalid value !!")

print("1. rock\n2. paper\n3. scissors")
choice = input("Please enter 2 digit choice by combining above numbers : ")
choice_lst = []
for i in choice:
    i = int(i)
    choice_lst.append(i)
if len(choice_lst) == 2:
    hand1 = choices(choice_lst[0])
    hand2 = choices(choice_lst[1])
    print(f"Entered choices are : {hand1} and {hand2}\n")
    result(hand1, hand2)
else:
    print("Enter value should be only 2 digit !!")
