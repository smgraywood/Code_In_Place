Write a program that has Karel draw a diagonal line across the world, with a slope of ½, like so:

An example end state of Karel walking up a ramp. The world has 7 rows and 7 columns,  with beepers at row 1 column 1, row 3 column 2, row 5 column 3, and row 7 column 4. Karel is at row 7 column 4 facing East.
The key to drawing a diagonal line with slope ½ is to move two steps forward and one step up between each beeper. In this problem you can and should assume that the world is an odd number of columns across. Solving the problem for even columns as well is much harder and would count as an "extension".


You should assume

Karel always begins at the bottom left corner of and empty world facing East.

You may assume that the world is an odd number of columns across

Karel's bag has infinite beepers.

It does not matter which direction Karel ends up facing.

The world is always square (the world's height is the same as its width)

We've provided you three worlds on which to test your code. You can toggle between them by changing the very last line in the file from run_karel_program('RampKarel1.w') to run_karel_program('RampKarel2.w') or run_karel_program('RampKarel3.w') -- you will likely need to press Run (it's fine if you do so without any code written) for the world change to take effect. RampKarel1 is a 7x7 world, RampKarel2 is a 3x3 world, and RampKarel3 is a 25x25 world.

------------

"""
File: RampClimbingKarel.py
--------------------
When you finish writing this file, RampClimbingKarel should be
able to draw a line with slope 1/2 in any odd sized world
"""

def main():
    while front_is_clear():
        put_beeper()
        move()
        move()
        turn_left()
        move()
        turn_right()
    put_beeper()

def turn_right():
    for i in range(3):
        turn_left()

    """
    In this world Karel will build a ramp out of beepers with a slope of 1/2.
    """

if __name__ == '__main__':
    run_karel_program('RampKarel1.w')
