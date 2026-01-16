from game_functions import pick_value

def play_game_1(min_x=0, max_x=20):
    
    print("Welcome to Game 1: 'Guess the Number'")
    print(f"Please think of a number between {min_x} and {max_x}")
    input("Press enter when you have chosen your number (do not tell me it!)\n")
    poss_values = list(range(min_x,max_x+1))
    
    game_ended = False

    n = 0
    
    while game_ended == False:
        # select a guess at random
        guess = pick_value(poss_values)
        n += 1
        print()
        print(f"Guess #{n}:")
        result = take_user_input(guess)
        
        if result==1:
            game_ended = True
        elif result==2:
            poss_values = [ x for x in poss_values if x < guess ]
        elif result==3:
            poss_values = [ x for x in poss_values if x > guess ]

        if len(poss_values) == 0:
            print("I got confused... Let me try again.")
            poss_values = list(range(min_x,max_x+1))

    print()
    print(f"That was fun!\nI took {n} guesses...\nThanks for playing\nGoodbye!")
    
def take_user_input(guess):
    print(f"My guess is that your number is {guess}. Was I right?")
    print(f"1 - Yes that was my number!")
    print(f"2 - No my number is lower than {guess}")
    print(f"3 - No my number is higher than {guess}")
    answer = None
    while answer not in ["1","2","3"]:
        answer = input("Please enter option 1 2 or 3\n> ")
    return int(answer)


if __name__ == "__main__":
    play_game_1()
