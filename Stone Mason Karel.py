Your next task is to repair the damage done to the Stanford Main Quad in the 1989 Loma Prieta earthquake. In particular, Karel should repair a set of arches where some of the stones (represented by beepers, of course) are missing from the columns supporting the arches, as illustrated in the figure below.

An initial example world with 8 rows, 13 columns, and broken arches that StoneMasonKarel must repair. There are  broken columns (vertical lines of beepers, with gaps) in columns 1, 5, 9, and 13.
Your program should work on the world shown above, but it should be general enough to handle any world that meets the basic conditions outlined at the end of this problem.

There are three example worlds here, and your program should work correctly in all of them. You can toggle between them by changing the very last line in the file from run_karel_program('SampleQuad1.w') to run_karel_program('SampleQuad2.w') or run_karel_program('SampleQuad3.w') -- you will likely need to press Run (it's fine if you do so without any code written) for the world change to take effect.


When Karel is done, the missing stones in the columns should be replaced by beepers, so that the final picture resulting from the initial world shown in Figure 5 would look like the illustration below.

Karel should repair the Main Quad to a structurally sound state after completion. The world is the same as previously, but the columns have been repaired so that columns 1, 5, 9 and 13 have beepers from rows 1 through 5 (there are walls between rows 5 and 6 which represent the upper bound of each column).

Karel’s final location and the final direction Karel is facing at the end of the run do not matter. Karel may count on the following facts about the world:

Karel starts at the corner where 1st Avenue and 1st Street meet, facing east, with an infinite number of beepers in Karel’s beeper bag. The first column should be built on 1st Avenue.

The columns are always exactly four Avenues apart, so they would be built on 1st Avenue, 5th Avenue, 9th Avenue, and so on.

The final column will always have a wall immediately after it. Although this wall appears after 13th Avenue in the example figure, your program should work for any number of beeper columns.

The top of a beeper column will always be marked by a wall. However, Karel cannot assume that columns are always five units high, or even that all columns within a given world are the same height.

In an initial world, some columns may already contain beepers representing stones that are still in place. Your program should not put a second beeper on corners that already have beepers. Avenues that will not have columns will never contain existing beepers.


Note: if you're missing the additional "1x1.w" and "21x21.w" world files, you can download these files below, and then add/upload them to your challenge workspace:

File
1x1.w
File
21x21.w
Alternatively, save a copy of your code first, and you can then use the ... > Reset to Scaffold in the top right to update automatically. All files will be reset back to their original state, so be careful.

--------

"""
File: StoneMasonKarel.py
------------------------
When you finish writing code in this file, StoneMasonKarel should be
able to solve the "repair the quad" problem from Assignment 1.
You should make sure that your program works for all of the
sample worlds supplied in the starter code.
"""

def main():
    while front_is_clear():
        build_column()
        for i in range(4):
            move()
    build_column()

def build_column():
    turn_left()
    while front_is_clear():
        if no_beepers_present():
            put_beeper()
        move()
    turn_left()
    turn_left()
    if no_beepers_present():
        put_beeper()
    while front_is_clear():
        move()
    turn_left()
    
""" In this program, Karel will be building several columns 
via a while loop and a newly defined build_column function.
"""

if __name__ == '__main__':
    run_karel_program('SampleQuad1.w')
