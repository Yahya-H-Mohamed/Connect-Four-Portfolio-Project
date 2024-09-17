"""
Step 1
Determine whether to play against computer or another player
"""
def choose_opponent():
    """
    This function asks the user whether they would like
    to play against the computer or against another
    player. It will force the user to re-enter their 
    answer if they entered an invalid input
    """
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
        choose_pponent()

"""
Step 2
Create and print Board game
"""
game_board = []

def generate_board():
    """
    This function will append an array 
    for each row of the game board
    """
    for i in range(7):
        game_board.append(["( )","( )","( )","( )","( )","( )","( )"])

def display_board():
    """
    This function will print each joined list in the
    game_board list
    """
    for i in range(len(game_board)):
        print(" ".join(game_board[i]))

def play_against_player():
    player

def main():
    choose_opponent()
    generate_board()
    display_board()

main()