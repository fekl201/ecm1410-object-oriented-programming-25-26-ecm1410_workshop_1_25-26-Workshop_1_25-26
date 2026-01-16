from game_functions import process_guess

import random

def play_game_3(n_lives=10):

    print("Welcome to Game 3: Hangman!")
    print(f"You have {n_lives} lives to try to guess the secret word!")

    with open("words.txt") as f:
        wordlist = f.read().splitlines()

    word = random.choice(wordlist)

    board = ["_",] * len(word)

    letters_guessed = []

    game_finished = False

    n_remaining = n_lives

    while game_finished==False:
        input("Press enter to continue\n> ")
        print("-"*50)
        print(f"The board is: {" ".join(board)}")
        print("-"*50)
        print(f"Guessed letters: {" ".join(letters_guessed)}")
        print(f"You have {n_remaining} lives left.")
        print()
        print("What letter would you like to guess?.")
        letter = ""
        while (len(letter) != 1) or (letter not in "abcdefghijklmnopqrstuvwxyz"):
            letter = input("Enter a letter (a-z)\n> ")
    
        letters_guessed.append(letter.lower())
        result = process_guess(letter, board, word)
        if result == False:
            n_remaining += -1

        if "".join(board) == word:
            print()
            print("-"*50)
            print(f"You won! The word was {word}")
            print("-"*50)
            game_finished = True

        if n_remaining == 0:
            print()
            print("-"*50)
            print(f"You lost! The word was {word}")
            print("-"*50)
            game_finished = True


if __name__ == "__main__":
    play_game_3()
