Write a program in the file subtract_numbers.py that reads two real numbers from the user and prints the first number minus the second number.

You can assume the user will always enter valid real numbers as input (negative values are fine). Yes, we know this problem is really similar to a problem we did in class – that’s why this problem is a sandcastle!

A sample run of the program is shown below (user input is in bold italics):

$ python subtract_numbers.py
This program subtracts one number from another.
Enter first number: 5.5
Enter second number: 2.1
The result is 3.4

--------

import math
def main():
    print("This program subtracts one number from another.")
    input1= input("Enter first number: ")
    input1= float(input1)
    input2=input("Enter second number: ")
    input2= float(input2)
    total= input1 - input2
    print("The result is " + str(input1 - input2))

if __name__ == '__main__':
    main()
