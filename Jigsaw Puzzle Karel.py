During quarantine, Karel has picked up a new hobby: doing puzzles! Karel is almost done with the square puzzle represented by the 4x4 grid of beepers shown below:


The beeper in the bottom most row represents the last piece of the puzzle! Write a program which will get Karel to pick up the last piece, put it in place, and move Karel back to the bottom left corner of the world facing East so she can admire the completed puzzle. Here's what your end result should look like:


To reiterate, you should write the sequence of commands so that Karel will:

Move to and pick up the last puzzle piece (the beeper in row 1, column 3)

Put the puzzle piece in place (row 3, column 4)

Return Karel to her initial position

Although the program does not have many lines of code, it is still worth getting some practice with decomposition. In your solution, include a function for each of the three steps shown in the outline above.

--------

"""
File: PuzzleKarel.py
--------------------
Karel should finish the puzzle by picking up the last beeper (puzzle piece) and placing it in the right spot.
Karel should end in the same position Karel starts in -- the bottom left corner of the world.
"""

def main():
    movex2()
    pick_beeper()
    turn_left()
    move()
    turn_right()
    move()
    turn_left()
    move()
    put_beeper()
    turn_right()
    turn_right()
    movex2()
    turn_right()
    movex2()
    move()
    turn_left()
    turn_left()


def turn_right():
    turn_left()
    turn_left()
    turn_left()
def movex2():
    move()
    move()
#Karel completes the puzzle
    pass

if __name__ == '__main__':
    run_karel_program('Puzzle.w')
