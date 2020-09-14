import random

guessed_letters = []
is_correct = True

file = open("words.txt", "r")
# convert txt file stuff into strings and put those into a list here
my_list = file.read()
words = my_list.split()
file.close()

word = list(random.choice(words))  # Pick a random word from the text file
hint = list('_' * len(word))

guesses = 0


def print_hint():
    for hints in hint:
        print(hints, end="", flush=True)


def game_over():
    global letter
    if guesses == 6:
        print("\n\nThe word was:")
        for letter in word:
            print(letter, end="", flush=True)
        print()
        print("\n----------")
        print("|YOU LOSE|")
        print("----------")
        print(print_hangman(6))
        return True

    if '_' not in hint:
        print("\n---------")
        print("|YOU WIN|")
        print("---------")
        return True


def print_hangman(stage):
    hangman_pics = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']
    return hangman_pics[stage]


if __name__ == '__main__':
    print_hint()
    while not game_over():
        print(print_hangman(guesses))
        user_guess = input("\n\nGuess your letter: ").upper()
        index = 0
        if len(user_guess) > 1:
            print("You can choose only one letter at a time")
        else:
            if user_guess in guessed_letters:
                print("You already guessed this letter before")

            for letter in word:
                if user_guess in word[index]:
                    hint[index] = word[index]
                    guessed_letters.append(user_guess)
                    print(hint[index], end="", flush=True)
                    is_correct = True
                else:
                    is_correct = False
                    print(hint[index], end="", flush=True)
                index += 1

            if not is_correct and user_guess not in guessed_letters:
                print("\nIncorrect!", end="")
                guessed_letters.append(user_guess)
                is_correct = True
                guesses += 1



