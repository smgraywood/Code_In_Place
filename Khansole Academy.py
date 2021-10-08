Now that you’ve seen how programming can help us in a number of different areas, it’s time for you to implement Khansole Academy—a program that helps other people learn! In this problem, you’ll write a program in the file khansole_academy.py that randomly generates a simple addition problem for the user, reads in the answer from the user, and then checks to see if they got it right or wrong. Note that “console” is another name for “terminal” :-).

More specifically, your program should be able to generate simple addition problems that involve adding two 2-digit integers (i.e., the numbers 10 through 99). The user should be asked for an answer to the generated problem. Your program should determine if the answer was correct or not, and give the user an appropriate message to let them know.

A sample run of the program is shown below (user input is in bold italics).

$ python khansole_academy.py
What is 51 + 79?
Your answer: 120
Incorrect. The expected answer is 130
Here's another sample run, where the user gets the question correct:

$ python khansole_academy.py
What is 55 + 11?
Your answer: 66
Correct!

----------


import random 

def main():   
    count=0     
    while True: 
        a = random.randint(0,100)
        b = random.randint(0,100)
        c = print("What is " + (str(a)+' + '+str(b)+ "?"))
        d= input("Your answer: ")
        if int(d) == a+b:
            print("Correct!")
            count += 1
        else:
            print("Incorrect. The expected answer is: " + str(a+b))
        break 

if __name__ == '__main__':
    main()
