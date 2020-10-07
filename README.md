# Sudoku puzzle

This is a sudoku puzzle desktop application. It allows its users to take
on a challenge of randomly generated sudoku puzzles on three difficulty
levels. Players are awarded points for solving the puzzle. The number
of points they get varies depending on how quickly were they able to solve
the puzzle, number of hints they used, and the difficulty setting they have
chosen. Multiple users can create their unique accounts and compare their
high scores between themselves.

This project posed an interesting challenge, as it encapsulated a wide range
of programming problems - from a backtracking algorithm employed to generate
and solve sudoku puzzles, to building a graphical user interface with Tkinter.

# Installation

To run the program, it is necessary to download all the files in this
repository. Moreover, it is required that Python 3 is installed on the
user's computer. In addition to this, two third-party libraries need to
be installed: Tkinter and NumPy.

Having those installed, it is required to extract all the files into the same
folder. It is then necessary to navigate into that directory using the command
line and then run the "main.py" script using the "python" command.

# Technology

The whole project was developed with Python 3.7. It was split into two
packages: backend and frontend.

The backend package consists of three modules. One of them 
("sudoku_solver.py") is based on the backtracking algorithm that allows for
solving solvable sudoku grids. Another one ("sudoku_generator.py") builds on
that functionality to randomly generate solvable grids. Finally, the remaining
one("aux_sudoku_funcs") contains auxilary functions that are used in both of 
the aforementioned modules.

The frontend package was developed using the Tkinter library. Similarly,
it is made of three modules. "game_screen.py" is responsible for the main
functionality of the program. It is where the users select the difficulty
setting, generate the puzzle, and attempt to solve it. "login_screen.py"
builds the graphical interface of the welcome screen. It is where the users
can register, select an existing username, check the leaderboard and start
a game. Finally, "other_screens.py" contains classes responsible for the
leaderboard screen and the win screen (that pops up when the puzzle is
successfuly solved).

User data is stored in the "users.json" file. It is not to be deleted
or manipulated.

# Common issues

Due to the nature of how the puzzles are generated (emptying spots of a filled
sudoku grid one by one from randomly selected coordinates while checking that
a resultant grid still leads to a single solution) it may sometimes take
an excessive amount of time to generate a puzzle on an "Advanced" level (the
diffculty levels are determined by the number of spots already filled). Should
that happen, it is best to terminate the program (ctrl + Pause/Break) and
restart it.

 