import array
import random


def generate_password(char_count, symbol_count, number_count):
    letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
                     'I', 'J', 'K', 'M', 'N', 'O', 'P', 'Q',
                     'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y',
                     'Z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',
                     'i', 'j', 'k', 'm', 'n', 'o', 'p', 'q',
                     'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
                     'z']
    symbols = ['@', '#', '$', '%', '=', ':', '?', '.', '/', '|', '~', '>',
           '*', '(', ')', '<']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    combined_letters = []

    for i in range(char_count):
        l = random.choice(letters)
        combined_letters.append(l)
    for i in range(symbol_count):
        s = random.choice(symbols)
        combined_letters.append(s)
    for i in range(number_count):
        n = random.choice(numbers)
        combined_letters.append(n)

    random.shuffle(combined_letters)

    password = ''.join(combined_letters)

    return password


char_count = int(input("Enter count of letters you want in password :"))
symbol_count = int(input("Enter count of symbols you want in password :"))
number_count = int(input("Enter count of numbers you want in password : "))
password = generate_password(char_count, symbol_count, number_count)

print("Here is your required password : ", password)