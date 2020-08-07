# games

We are going to build a two-player tic-tac-toe game, which we can play in the GUI (made by tkinter).
Initially, we’ll make an empty game board and then we’ll take inputs from the players and we’ll check for the winning condition.
if the whole board gets filled and no one wins, we’ll declare the result as “Draw” and restart the game.
The game is restarted after every match results.

We will build this game using Python 3 and tkinter tools for GUI.
First of all, define the tk window with the Tk() as the root variable.
Then we create the title of the window.
Next, we define a variable to store the playable character(say, ‘O’ and ‘X’ at random).
Then we define a list to store all the buttons and place them in the window.
Finally, we display a label saying the character which has to be played next.
We end by a root.mainloop() function to keep events on the main window active and all other widgets interactive.
