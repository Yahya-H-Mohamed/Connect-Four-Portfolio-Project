# Connect 4

Connect 4 is a python terminal game. The game involves two players, either a player against the computer or two live players, competing to be the first person to get 4 consecutive tokens stacked horizontally, vertically or diagonally.

[Click here to play the live project](to be entered)

## Planning
To plan for this project I wrote psuedocode to help me get a rough idea of what steps to take when building the game.

![Psuedocode](/assets/images/psuedocode.png)

## Project Objectives
When building this project I set a few goals to check off upon completing it

- Allow users to play against a friend locally

- - To achieve this objective I built a function that takes an input from the user. The user is given 2 options, player or computer. Upon inputting the correct value for the player mode, the versus_player function is called. This function takes the names of both players and then runs the gameplay loop, alternating turns between each player.

- Allow users to play against a computer (To prevent a minimum 2 person limit)

- - Similarly to the versus player mode, I built another function that is called when the user chooses the versus computer option. This function works like the versus player one however, instead of there being two players taking turns to input a column, the computer randomly generates a number and that number is used as their choice of column

- Keep gameplay fluid and clear (Regularly update board, inform users of their turn)

- - To achieve this I created the display_board function, this function prints out a joined list of the game board. This function is called after every turn because after a turn, the game board is updated. So to give users a visual on what happened in the previous turn, the board is displayed.

- Target Audience
- - Connect 4 is a classic board game almost everyone has played before at some point. That is one of the reasons I chose to build it for this project. It was a game that is very easy to grasp and is mainly targetted at children but can be played by people of all ages. The instructions I wrote in the program are simplified because most people know how to play but if they have not then they can still read the brief summary. Most young people have friends that come over to play, hence I added a local multiplayer mode to the game. Additionally those who just want to play connect 4 but don't have anyone to play with can still enjoy the versus computer single player mode.

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

## Planned Features
- Better computer intelligence
- Multiple token icons for players to choose from

## Testing
The tests I have carried out on this project are:

- I have entered different inputs for all scenarios to ensure I have caught all potential input errors
- I have passed my code through PEP8 linter with no issues
- Run and test my code in the local terminal
- Run and test my code in the Heroku terminal

### Fixed Bugs
- During gameplay, in some cases the win condition was not running even though 4 tokens were successfully stacked in a row. I tested this is all game modes and this issue was reoccuring. To fix this I used the win condition loops in the determine_winner function to place a token in every empty space on the board. When doing this I discovered that there was a logic error in my loop range condition and it was not covering every column and row on the board. After correcting this mistake the win condition was correctly running as intended.

### Current Bugs
There are currently no remaining bugs I could find when testing and running my code

## Deployment
This project was deployed using Code Institutes mock terminal for Heroku.

- Steps for deployment
- - Fork or Clone this repository
- - Create a new Heroku application
- - Set the buildpack to Python and NodeJS in that order
- - Link the Heroku app to the repository
- - Click on Deploy

## Credits
- Code institute for the deployment terminal
- Hasbro Website for Connect 4 instructions