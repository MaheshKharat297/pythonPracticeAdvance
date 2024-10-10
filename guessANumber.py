import random

def compare_number(original_number):
    guessed_number = int(input("Please guess the number :"))
    if original_number > guessed_number:
        print("Your guess is too low")
        return False
    elif original_number < guessed_number:
        print("Your guess is too high")
        return False
    else:
        return True

def difficulty(difficulty_level):
    if difficulty_level == "hard":
        return 5
    elif difficulty_level == "easy":
        return 10
    else:
        print("Invalid input")
        return 0


if __name__ == '__main__':
    print("Let me think of a number between 1 to 50.")
    original_number = random.randint(1, 50)
    difficulty_level = input("Please select difficulty level between easy and hard : ")
    life_lines = difficulty(difficulty_level)
    print(f"You have {life_lines} lifes !!")

    flag = True
    while flag:
        result = compare_number(original_number)
        if result == True:
            print("The number is perfectly matched !!!")
            print("Congratulation you won !!!")
            flag = False
        elif result == False and life_lines > 0:
            life_lines -= 1
            print(f"You remain with {life_lines} life now !")
            flag = True
        else:
            print("Out of lifelines, BYE........")
            print(f"The original number was {original_number}")
            flag = False