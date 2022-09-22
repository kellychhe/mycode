#!/usr/bin/env python3
"""using while loops"""

def main():

    # set a counter
    round = 0
    
    # create a loop
    while True:
        round = round + 1
        print('Finish the movie title, "Monty Python\'s The Life of ______"')
        answer = input("Your guess--> ")
        if answer == 'Brian':
            print("correct")
            break
        elif round == 3:
            print("Sorry, the answer was Brian.")
            break
        else:
            print("Sorry! Try again!")

if __name__ == "__main__":
    main()


