from game_functions import check_higher_lower

import random

def play_game_2(min_x=0, max_x=20):

    print("Welcome to Game 2: 'Higher or Lower'")
    print(f"The computer will generate a sequence of random numbers from {min_x} to {max_x}.")
    print("You have to guess whether the next number will be higher or lower")
    print("If you are wrong the game ends!")
    input("Press enter to continue\n> ")

    sequence = []

    x = random.randint(min_x,max_x)
    sequence.append(x)
    game_ended = False

    while game_ended == False:
        print()
        print(f"The current value is: {sequence[-1]}")
        print("Do you think the next number going to be higher (h) or lower (l)?")
        user_input = "NA"
        while user_input not in ["h", "l"]:
            user_input = input("Enter h or l:\n> ")
        
        current_val = sequence[-1]
        
        next_val = current_val
        while next_val == current_val:
            next_val  = random.randint(min_x,max_x)

        sequence.append(next_val)

        print()
        print(f"The next number is ... {next_val}")

        result = check_higher_lower(current_val, next_val, user_input)

        if result == True:
            print("Well done - you survived!")
            print(f"Sequence so far has {len(sequence)} terms:")
            print(sequence)
            input("Press enter to continue\n> ")
        else:
            print("Sorry - game over!")
            print(f"You built a sequence with {len(sequence)} terms:")
            print(sequence)
            print("Thanks for playing...")
            print("Bye!")
            game_ended = True
            
                 
if __name__ == "__main__":
    play_game_2()
