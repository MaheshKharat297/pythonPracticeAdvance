from random_word import RandomWords
def generate_word():
    r = RandomWords()
    word = r.get_random_word()
    return word

def word_check(letter, word):
    if letter in word:
        return True
    return False

def word_placement(letter, word, final_word_lst, word_count):
    #print(word)
    for position in range(len(word)):
        l = word[position]
        if l == letter:
            final_word_lst[position] = letter
            word_count += 1

    final_word = ' '.join(final_word_lst)
    return final_word, word_count

def hangman(life_lines):
    if life_lines==0:
        print('''
                ------------|
                 |          |
                 0          |
                /|\         |
                / \         |
                           _|_
                ''')
    elif life_lines==1:
        print('''
                ------------|
                 |          |
                 0          |
                /|\         |
                /           |
                           _|_
                ''')
    elif life_lines==2:
        print('''
                ------------|
                 |          |
                 0          |
                /|\         |
                            |
                           _|_
                ''')
    elif life_lines==3:
        print('''
                ------------|
                 |          |
                 0          |
                /|          |
                            |
                           _|_
                ''')
    elif life_lines==4:
        print('''
                ------------|
                 |          |
                 0          |
                 |          |
                            |
                           _|_
                ''')
    elif life_lines == 5:
        print('''
                   ------------|
                    |          |
                    0          |
                               |
                               |
                              _|_
                   ''')
    else:
        print('''
                   ------------|
                    |          |
                               |
                               |
                               |
                              _|_
                   ''')

print("Lets play HANGMAN !!!")
print("You have 6 life lines only !!!")

word = generate_word()
for i in range(len(word)):
    print("_", end=' ')

word_length = len(word)
life_lines = 6
final_word = ""
word_count = 0
final_word_lst = []
guessed_lst = []
for i in word:
    final_word_lst.append("_")

for i in range(word_length*2):
    letter = input("\n\nPlease enter the letter :")
    if letter not in guessed_lst:
        guessed_lst.append(letter)
        result = word_check(letter, word)
        if result == True and life_lines > 0:
            final_word, word_count = word_placement(letter, word, final_word_lst, word_count)
            print(final_word)
            if word_count == word_length:
                print("Completed Successfully !!")
                hangman(life_lines)
                break

        elif life_lines == 0:
            print("Game Over !!")
            hangman(life_lines)
            print("The word was : ", word)
            break
        else:
            life_lines = life_lines - 1
            print("Sorry wrong word, Lifeline gone !!!")
            print("Remaining lifes : ", life_lines)
            hangman(life_lines)
    else:
        print("Already guessed !!")

