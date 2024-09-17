"""
Step 1
Determine whether to play against computer or another player
"""
def chooseOpponent():
    print("Would you like to play against the computer or another player")
    print("Type 'c' for computer")
    print("Type 'p' for player")

    opponent = input("Enter: ")

    if opponent.lower() == "c":
        #play against computer function goes here
        print("Your opponent will be the computer\n")
    elif opponent.lower() == "p":
        #play against player function goes here
        print("Your opponent will be a player\n")
    else:
        print("Incorrect input. Please enter one of the valid options provided\n")
        chooseOpponent()

chooseOpponent()