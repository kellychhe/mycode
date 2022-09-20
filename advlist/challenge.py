#!/usr/bin/env python3

from random import randint

"""list challenge!"""

def main():

    wordbank = ["indentation", "spaces"]

    tlgstudents= ["Aaron", "Andy", "Asif", "Brent", "Cedric", "Chris", "Cory", "Ebrima", "Franco", "Greg", "Hoon", "Joey", "Jordan", "JC", "LB", "Mabel", "Shon", "Pat", "Zach"]

    # part 3: appends the integer 4 to the list wordbank
    wordbank.append(4)

    # part 4: ask for number between 0 and 18, a name, or randomizer
    method = input("Enter a number between 0 and 18 or a valid name, otherwise the computer will choose for you:  ")

    # part 5: convert num into an integer
    # check which method to use and assign name accordingly
    if method.isdigit() and method != "":
        name = tlgstudents[int(method)]
    elif method in tlgstudents:
        name = method
    else:
        random = randint(0,18)
        name = tlgstudents[random]
    
    # part 6: print output using elements from tlgstudents and wordbank
    print(f"{name} always uses {wordbank[2]} {wordbank[1]} to indent.")

if __name__ == "__main__":
    main()
