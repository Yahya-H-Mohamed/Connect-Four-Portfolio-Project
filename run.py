import random

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
        print("Your opponent will be the computer\n")
        versus_computer()
    elif opponent.lower() == "p":
        print("Your opponent will be a player\n")
        versus_player()
    else:
        print("Incorrect input. Please enter one of the valid options provided\n")
        choose_opponent()

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
        game_board.append(["(  )","(  )","(  )","(  )","(  )","(  )","(  )"])

def display_board():
    """
    This function will print each joined list in the
    game_board list
    """
    for i in range(len(game_board)):
        print(" ".join(game_board[i]))

"""
Step 3

Build game logic for player vs player mode.
"""

def versus_player():
    player_one = input("Enter the first players name: ")
    player_two = input("Enter the second players name: ")

    player_turns = 1 

    while True:
        if player_turns % 2 != 0:
            display_board()

            print(f"It is {player_one}'s turn (🔵)")
            player_one_turn = int(input("Please enter a column you would like to place your token: "))
            player_one_turn -= 1

            while True:
                if game_board[0][player_one_turn] != "(  )":
                    print("That column is full. Please choose another column you would like to place your token")
                break
                    
            for number in range(6,-1,-1):
                if game_board[number][player_one_turn] == "(  )":
                    game_board[number][player_one_turn] = "(🔵)"
                    player_turns += 1
                    break 
        else:
            display_board()

            print(f"It is {player_two}'s turn (🔴)")
            player_two_turn = int(input("Please enter a column you would like to place your token: "))
            player_two_turn -= 1

            while True:
                if game_board[0][player_two_turn] != "(  )":
                    print("That column is full. Please choose another column you would like to place your token")
                break

            for number in range(6,-1,-1):
                if game_board[number][player_two_turn] == "(  )":
                    game_board[number][player_two_turn] = "(🔴)"
                    player_turns += 1
                    break    

"""
Step 3 

Build game logic for player vs computer mode
"""
def versus_computer():
    player_one = input("Enter your name: ")

    player_turns = 1 

    while True:
        if player_turns % 2 != 0:
            display_board()

            print(f"It is {player_one}'s turn (🔵)")
            player_one_turn = int(input("Please enter a column you would like to place your token: "))
            player_one_turn -= 1

            while True:
                if game_board[0][player_one_turn] != "(  )":
                    print("That column is full. Please choose another column you would like to place your token")
                break
                    
            for number in range(6,-1,-1):
                if game_board[number][player_one_turn] == "(  )":
                    game_board[number][player_one_turn] = "(🔵)"
                    player_turns += 1
                    break 
        else:
            display_board()

            print(f"It the computer's turn (🔴)")
            computers_turn = random.randint(0, 6)
            print(f"The computer chose: {computers_turn + 1}")

            while True:
                if game_board[0][computers_turn] != "(  )":
                    print("Oops! The computer chose a column that was full. It will try again")
                break

            for number in range(6,-1,-1):
                if game_board[number][computers_turn] == "(  )":
                    game_board[number][computers_turn] = "(🔴)"
                    player_turns += 1
                    break


def main():
    generate_board()
    choose_opponent()

main()