# Connect 4

Connect 4 is a python terminal game. The game involves two players, either a player against the computer or two live players, competing to be the first person to get 4 consecutive tokens stacked horizontally, vertically or diagonally.

[Click here to play the live project](to be entered)

## How To Play

My Connect 4 game follows the same rules as the classic connect 4 board game. Two players place tokens into a 7x6 grid until one of the players stacks 4 consecutive tokens going in any direction.

In this project, the user gets the option to play with a friend (locally) or against the computer.

If the user chose to play against another player, they will have the choice to enter a name followed by the second player getting the same option. However if the user chose to compete against the computer they will enter only their name. The computer opponent is labelled "Computer.

Player (1) will always have the first turn are are assigned the token "🔵". The second player/computer are assigned the token "🔴".

Each turn the current player is given the choice between 7 columns to place their token into. The first player to get 4 of their tokens next to each other, horizontally, vertically or diagonally wins.

## Features
- Versus Player Mode
- Versus Computer Mode
- Updates and displays the game board after every turn

	![Image showing board display functionality after every turn](/assets/images/Display.png)

- Input Validation
- - Cannot enter a number below 1 or above 7 or non number characters

	![Image showing input validation for numbers below 1, above 7 and non number inputs](/assets/images/Validation.png)

- - Cannot choose a column when it is full

	![Image showing input validation when user selects a column that is already full](/assets/images/Full-column.png)