import random  # This will be used in the versus computer mode

game_board = []  # This will hold the connect 4 tokens


def choose_opponent():
    """
    This function asks the user whether they would like
    to play against the computer or against another
    player. It will force the user to re-enter their
    answer if they entered an invalid input
    """
    print("Welcome to Connect 4")
    print("First to get 4 tokens consecutively stacked in any direction wins!")
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
        print("Invalid input. Please enter one of the valid options\n")
        choose_opponent()


def generate_board():
    """
    This function will append an array
    for each row of the game board
    """
    for i in range(6):
        # Each row will be added to the game board list
        game_board.append(["(  )"] * 7)


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
    running_game = True  # Determines whether loop should continue or terminate

    while True:
        try:
            # First players name
            player_one = input("Enter the first players name: ")
            # Second players name
            player_two = input("Enter the second players name: ")
            if len(player_one) == 0 or len(player_two) == 0:
                raise ValueError(f"Please enter a name")
            else:
                break
        except ValueError as e:
            print(f"Invalid input: {e}, please try again. \n")

    # This variable will determine which players turn it is
    player_turns = 1

    while running_game:
        if player_turns % 2 != 0:
            display_board()

            print(f"It is {player_one}'s turn (🔵)")
            while True:
                try:
                    player_one_input = int(input("Enter a column(1-7): "))
                    valid_answer = [1, 2, 3, 4, 5, 6, 7]
                    if player_one_input not in valid_answer:
                        raise ValueError(f"The value must be between 1 and 7.")
                    else:
                        player_one_input -= 1
                        break
                except ValueError as e:
                    print(f"Invalid input: {e}, please try again. \n")

            while True:
                # If the column is full they must choose another column
                if game_board[0][player_one_input] != "(  )":
                    print("That column is full. Choose another column.")
                break

            # This loop checks every space on the board
            for number in range(5, -1, -1):
                # If the space the player chose is empty
                if game_board[number][player_one_input] == "(  )":
                    # Input their token
                    game_board[number][player_one_input] = "(🔵)"
                    # If any of the win conditions returns true
                    if determine_winner(player_one, "(🔵)"):
                        running_game = False  # End game
                    elif draw_state():  # If the draw condition returns true
                        running_game = False  # End game
                    else:  # If neither of those are true the game continues
                        player_turns += 1
                    break  # Current turn ends
        else:
            display_board()

            print(f"It is {player_two}'s turn (🔴)")
            while True:
                try:
                    player_two_input = int(input("Enter a column(1-7): "))
                    valid_answer = [1, 2, 3, 4, 5, 6, 7]
                    if player_two_input not in valid_answer:
                        raise ValueError(f"The value must be between 1 and 7.")
                    else:
                        player_two_input -= 1
                        break
                except ValueError as e:
                    print(f"Invalid input: {e}, please try again. \n")

            while True:
                # If the column is full they must choose another column
                if game_board[0][player_two_input] != "(  )":
                    print("That column is full. Choose another column.")
                break

            # This loop checks every space on the board
            for number in range(5, -1, -1):
                # If the space the player chose is empty
                if game_board[number][player_two_input] == "(  )":
                    # Input their token
                    game_board[number][player_two_input] = "(🔴)"
                    # If any of the win conditions returns true
                    if determine_winner(player_two, "(🔴)"):
                        running_game = False  # End game
                    elif draw_state():  # If the draw condition returns true
                        running_game = False  # End game
                    else:  # If neither of those are true the game continues
                        player_turns += 1
                    break  # Ends current player turn


def versus_computer():
    """
    This function will take the name and positional inputs from
    the player and computerand push them to the game board. If
    the determine winner function returns true then the loop will
    be broken.
    """
    running_game = True  # Determines whether loop should continue or terminate

    while True:
        try:
            # Enter player name
            player = input("Enter your name: ")
            if len(player) == 0:
                raise ValueError(f"Please enter a name")
            else:
                break
        except ValueError as e:
            print(f"Invalid input: {e}, please try again. \n")

    player_turns = 1  # This variable will determine which players turn it is

    while running_game:
        if player_turns % 2 != 0:
            display_board()

            print(f"It is {player}'s turn (🔵)")
            while True:
                try:
                    player_input = int(input("Enter a column(1-7): "))
                    valid_answer = [1, 2, 3, 4, 5, 6, 7]
                    if player_input not in valid_answer:
                        raise ValueError(f"The value must be between 1 and 7.")
                    else:
                        player_input -= 1
                        break
                except ValueError as e:
                    print(f"Invalid input: {e}, please try again. \n")

            while True:
                # If the column is full they must choose another column
                if game_board[0][player_input] != "(  )":
                    print("That column is full. Choose another column")
                break

            # This loop checks every space on the board
            for number in range(5, -1, -1):
                # If the space the player chose is empty
                if game_board[number][player_input] == "(  )":
                    # Input their token
                    game_board[number][player_input] = "(🔵)"
                    # If any of the win conditions returns true
                    if determine_winner(player, "(🔵)"):
                        running_game = False  # End game
                    elif draw_state():  # If the draw condition returns true
                        running_game = False  # End game
                    else:  # If neither of those are true the game continues
                        player_turns += 1
                    break  # Ends player turn
        else:
            display_board()

            print(f"It the computer's turn (🔴)")
            # Selects a random number between 0-6
            computer_input = random.randint(0, 6)
            print(f"The computer chose: {computer_input + 1}")

            while True:
                # If the column is full they must choose another column
                if game_board[0][computer_input] != "(  )":
                    print("The computer will choose another column")
                break

            # This loop checks every space on the board
            for number in range(5, -1, -1):
                # If the space the computer chose is empty
                if game_board[number][computer_input] == "(  )":
                    # Input their token
                    game_board[number][computer_input] = "(🔴)"
                    # If any of the win conditions returns true
                    if determine_winner("Computer", "(🔴)"):
                        running_game = False  # End game
                    elif draw_state():  # If the draw condition returns true
                        running_game = False  # End game
                    else:  # If neither of those are true the game continues
                        player_turns += 1
                    break  # Ends computer turn


def determine_winner(player, token):
    """
    This function will loop through all possible positions in the game board
    to check if there are atleast 4 consecutive tokens of the same type going
    in all directions. If there are it will return true.
    """
    # Column check
    for i in range(7):
        for j in range(3):
            if(game_board[j][i] == token and
               game_board[j + 1][i] == token and
               game_board[j + 2][i] == token and
               game_board[j + 3][i] == token):
                display_board()
                print(f"{player} WINS!!!")
                print("Thank you for playing Connect 4")
                return True

    # Row check
    for i in range(4):
        for j in range(6):
            if(game_board[j][i] == token and
               game_board[j][i + 1] == token and
               game_board[j][i + 2] == token and
               game_board[j][i + 3] == token):
                display_board()
                print(f"{player} WINS!!!")
                print("Thank you for playing Connect 4")
                return True

    # Diagonal check
    for i in range(3):
        for j in range(3, 7):
            if(game_board[i][j] == token and
               game_board[i + 1][j - 1] == token and
               game_board[i + 2][j - 2] == token and
               game_board[i + 3][j - 3] == token):
                display_board()
                print(f"{player} WINS!!!")
                print("Thank you for playing Connect 4")
                return True

    # Diagonal check (Reverse)
    for i in range(4):
        for j in range(3):
            if(game_board[j][i] == token and
               game_board[j + 1][i + 1] == token and
               game_board[j + 2][i + 2] == token and
               game_board[j + 3][i + 3] == token):
                display_board()
                print(f"{player} WINS!!!")
                print("Thank you for playing Connect 4")
                return True


def draw_state():
    """
    This function checks every space on the game
    board. If all spaces are occupied on the board
    it will return true.
    """
    # Holds the amount of occupied slots on board
    count = 0

    # This will loop through the entire board
    for i in range(6):
        for j in range(7):
            if game_board[i][j] != "(  )":  # If the current space is not full
                count += 1  # Increment the count by one

    # If every space is filled this will execute
    if count == 42:
        print(f"It was a draw. Game Over!")
        print("Thank you for playing Connect 4")
        return True


def main():
    """
    Runs functions
    """
    generate_board()
    choose_opponent()


main()
