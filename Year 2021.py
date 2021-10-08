Congratulations on beginning your coding journey! Karel welcomes you to Code in Place 2021. Your next task is to help Karel celebrate the occasion by placing 20 beepers, moving Karel one step, placing 21 beepers, and moving Karel one more step. The world should ultimately look like this:

A world with 3 rows and 3 columns, with 20 beepers in row 1 column 1 and 21 beepers in row 1 column 2. Karel is in row 1 column 3 facing East.
Happy coding!

-------

"""
File: 2021.py
--------------------
When you finish writing this file, Karel should be able to place 20 beepers,
then 21 beepers, and end facing East to the right of the 21 beepers.
"""

def main():
    put_beeper_20()
    move()
    put_beeper_20()
    put_beeper()
    move()

def put_beeper_20():
    put_beeper()
    put_beeper()
    put_beeper()
    put_beeper()
    put_beeper()
    put_beeper()
    put_beeper()
    put_beeper()
    put_beeper()
    put_beeper()
    put_beeper()
    put_beeper()
    put_beeper()
    put_beeper()
    put_beeper()
    put_beeper()
    put_beeper()
    put_beeper()
    put_beeper()
    put_beeper()
    """
    You should write your code to make Karel do its task in
    this function. Make sure to delete the 'pass' line before
    starting to write your own code. You should also delete this
    comment and replace it with a better, more descriptive one.
    """
    pass

if __name__ == '__main__':
    run_karel_program('3x3.w')
