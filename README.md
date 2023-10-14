# Tic-tac-toe-in-python
 A game which requires tricks


Tic-Tac-Toe is a two-player strategy game played on a 3x3 grid. The objective of the game is to get three of your symbols (either "X" or "O") in a row horizontally, vertically, or diagonally before your opponent does.

Game Logic:

Board Representation: In the code, the game board is represented as a 3x3 grid, initially filled with empty spaces.

Printing the Board: The print_board function is used to display the current state of the board in the console.

Winning Conditions: To check for a win, the code examines each row, column, and diagonal for three identical symbols in a row. If it finds a match, the game is won.

Draw Condition: The game can also end in a draw if all the spaces on the board are filled, and no player has won. The is_draw function checks for this condition.

Player Turns: The game alternates between two players, "X" and "O." The current_player variable keeps track of the current player's turn.

Game Loop: The game loop allows players to input their moves. It checks if the input is valid (within the grid and the cell is not already occupied) and updates the board accordingly. After each move, the code checks for a win or draw. If one of these conditions is met, the game ends.
