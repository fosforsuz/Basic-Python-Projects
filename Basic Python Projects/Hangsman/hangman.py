import random


def print_word():
    print(*user_guess, sep="")


def change_list(letter, word):
    lst = [index for index in range(len(word)) if word[index] == letter]
    for index in lst:
        user_guess[index] = letter


def control(guess_word, word, count_):
    message = ''
    for item in guess_word:
        message += item
    if message == word:
        print("You guessed the word!\nYou survived!")
        return True
    elif count_ == 0:
        print("You lost!")
        return True


def control_letter(letter, character):
    if letter in character:
        print("Please enter a lowercase English letter\n")
        return -1
    elif len(letter) == 0 or len(letter) > 1:
        print("You should input a single letter\n")
        return -1
    elif letter != letter.lower():
        print("Please enter a lowercase English letter\n")
        return -1


list_of_words = 'python', 'java', 'kotlin', 'javascript'
currently_word = random.choice(list_of_words)
user_guess = list("-" * len(currently_word))
guessed_letter = []
characters = list("!@#$%^&*()_+=-<>?|\\/1234567890[]{};:'\"~`,.")
count = 8
print("H A N G M A N\n")

while True:
    type_ = input("Type \"play\" to play the game, \"exit\" to quit: ")
    if type_ == "play":
        while True:
            print_word()
            if control(user_guess, currently_word, count):
                break
            guess = input("Input a letter: ")
            if control_letter(guess, characters) == -1:
                continue
            if guess in guessed_letter:
                print("You've already guessed this letter\n")
                continue
            elif guess in currently_word:
                change_list(guess, currently_word)
                guessed_letter.append(guess)
                print("\n")
            else:
                print(
                    "That letter doesn't appear in the word" if count == 1 else "That letter doesn't appear in the "
                                                                                "word\n")
                count -= 1
                guessed_letter.append(guess)
    elif type_ == "exit":
        break
