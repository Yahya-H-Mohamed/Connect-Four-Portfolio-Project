import random #This will be used in the versus computer mode

game_board = [] # This will hold the connect 4 tokens

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

def generate_board():
    """
    This function will append an array 
    for each row of the game board
    """
    for i in range(7):
        game_board.append(["(  )","(  )","(  )","(  )","(  )","(  )","(  )"]) # Each row will be added to the game board list

def display_board():
    """
    This function will print each joined list in the
    game_board list
    """
    for i in range(len(game_board)):
        print(" ".join(game_board[i]))

def versus_player():
    """
    This function will take the names and positional inputs,
    for each player and push them to the game board. If the determine
    winner function returns true then the loop will be broken.
    """
    running_game = True

    player_one = input("Enter the first players name: ")
    player_two = input("Enter the second players name: ")
    player_turns = 1 

    while running_game:
        if player_turns % 2 != 0:
            display_board()

            print(f"It is {player_one}'s turn (🔵)")
            while True:
                try:
                    player_one_input = int(input("Please enter a column you would like to place your token(1-7): "))
                    valid_answer = [1,2,3,4,5,6,7]
                    if player_one_input not in valid_answer:
                        raise ValueError(f"The value must be between 1 and 7. You chose {player_one_input}")
                    else:
                        player_one_input -= 1
                        break
                except ValueError as e:
                    print(f"Invalid input: {e}, please try again. \n")
            
            

            while True:
                if game_board[0][player_one_input] != "(  )":
                    print("That column is full. Please choose another column you would like to place your token")
                break
                    
            for number in range(6,-1,-1):
                if game_board[number][player_one_input] == "(  )":
                    game_board[number][player_one_input] = "(🔵)"
                    if determine_winner(player_one, "(🔵)"):
                        running_game = False
                    player_turns += 1
                    break 
        else:
            display_board()

            print(f"It is {player_two}'s turn (🔴)")
            while True:
                try:
                    player_two_input = int(input("Please enter a column you would like to place your token(1-7): "))
                    valid_answer = [1,2,3,4,5,6,7]
                    if player_two_input not in valid_answer:
                        raise ValueError(f"The value must be between 1 and 7. You chose {player_two_input}")
                    else:
                        player_two_input -= 1
                        break
                except ValueError as e:
                    print(f"Invalid input: {e}, please try again. \n")

            while True:
                if game_board[0][player_two_input] != "(  )":
                    print("That column is full. Please choose another column you would like to place your token")
                break

            for number in range(6,-1,-1):
                if game_board[number][player_two_input] == "(  )":
                    game_board[number][player_two_input] = "(🔴)"
                    if determine_winner(player_two, "(🔴)"):
                        running_game = False
                    player_turns += 1
                    break    

def versus_computer():
    """
    This function will take the name and positional inputs from
    the player and computerand push them to the game board. If 
    the determine winner function returns true then the loop will 
    be broken.
    """
    running_game = True

    player = input("Enter your name: ")
    player_turns = 1 

    while running_game:
        if player_turns % 2 != 0:
            display_board()

            print(f"It is {player}'s turn (🔵)")
            while True:
                try:
                    player_input = int(input("Please enter a column you would like to place your token(1-7): "))
                    valid_answer = [1,2,3,4,5,6,7]
                    if player_input not in valid_answer:
                        raise ValueError(f"The value must be between 1 and 7. You chose {player_input}")
                    else:
                        player_input -= 1
                        break
                except ValueError as e:
                    print(f"Invalid input: {e}, please try again. \n")

            while True:
                if game_board[0][player_input] != "(  )":
                    print("That column is full. Please choose another column you would like to place your token")
                break
                    
            for number in range(6,-1,-1):
                if game_board[number][player_input] == "(  )":
                    game_board[number][player_input] = "(🔵)"
                    if determine_winner(player, "(🔵)"):
                        running_game = False
                    player_turns += 1
                    break 
        else:
            display_board()

            print(f"It the computer's turn (🔴)")
            computer_input = random.randint(0, 6)
            print(f"The computer chose: {computer_input + 1}")

            while True:
                if game_board[0][computer_input] != "(  )":
                    print("Oops! The computer chose a column that was full. It will try again")
                break

            for number in range(6,-1,-1):
                if game_board[number][computer_input] == "(  )":
                    game_board[number][computer_input] = "(🔴)"
                    if determine_winner("Computer", "(🔴)"):
                        running_game = False
                    player_turns += 1
                    break

def determine_winner(player, token):
    """
    This function will loop through all possible positions in the game board
    to check if there are atleast 4 consecutive tokens of the same type going
    in all directions. If there are it will return true.
    """
    #This loop will check columns to see if 4 tokens are of the same type
    for i in range(7):
        for j in range(4):
            if(game_board[j][i] == token and game_board[j + 1][i] == token and game_board[j + 2][i] == token and game_board[j + 3][i] == token):
                display_board()
                print(f"{player} WINS!!!")
                print("Thank you for playing Connect 4")
                return True
    
    #This loop will check rows to see if 4 tokens are of the same type
    for i in range(4):
        for j in range(7):
            if(game_board[j][i] == token and game_board[j][i + 1] == token and game_board[j][i + 2] == token and game_board[j][i + 3] == token):
                display_board()
                print(f"{player} WINS!!!")
                print("Thank you for playing Connect 4")
                return True

    #This loop will check the game board diagonally to see if 4 tokens are of the same type
    for i in range(4):
        for j in range(3, 7):
            if(game_board[i][j] == token and game_board[i + 1][j - 1] == token and game_board[i + 2][j - 2] == token and game_board[i + 3][j - 3] == token):
                display_board()
                print(f"{player} WINS!!!")
                print("Thank you for playing Connect 4")
                return True
    
    #This loop will check the game board diagonally (backwards) to see if 4 tokens are of the same type
    for i in range(4):
        for j in range(4):
            if(game_board[j][i] == token and game_board[j + 1][i + 1] == token and game_board[j + 2][i + 2] == token and game_board[j + 3][i + 3] == token):
                display_board()
                print(f"{player} WINS!!!")
                print("Thank you for playing Connect 4")
                return True

def main():
    generate_board()
    choose_opponent()

main()