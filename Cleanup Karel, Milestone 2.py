Karel has a bit of spring cleaning to do! Karel's world will have beepers in some positions in the bottom row; write a program to have Karel walk across the bottom row and, at each position, pick up a beeper only if one is present. Notice that you've already written the code to check if a beeper is present and only pick up a beeper if one is there from the previous milestone -- you should use your code from the previous milestone as a helper function to help with the decomposition of this problem!

Additionally, note that Karel's starting position will never contain a beeper, so there's no need to check it.

For example, if this is the initial starting world, with some beepers in the first row:

A world with 5 rows and 5 columns. There are beepers in row 1 at columns 2, 4, and 5. Karel is at row 1 column 1 facing East.
This should be the end result, with a clear bottom row:

A 5x5 world with no beepers. Karel is in the bottom right corner, row 1 column 5, facing East.
We've provided you two worlds on which to test your code. You can toggle between them by changing the very last line in the file from run_karel_program('Cleanup1.w') to run_karel_program('Cleanup2.w') (and vice versa) -- you will likely need to press Run (it's fine if you do so without any code written) for the world change to take effect.

----------------------

"""
File: CleanupKarel.py
--------------------
When you finish writing this file, CleanupKarel should be able to
pick up all beepers from the first row of any sized world and
end in the bottom right corner facing East.
"""

def main():
    while front_is_clear():
        pick_beeper_cond()
    pick_beeper()

def pick_beeper_cond():
    if beepers_present():
        pick_beeper()
    else:
        move()

if __name__ == '__main__':
    run_karel_program('Cleanup2.w')
