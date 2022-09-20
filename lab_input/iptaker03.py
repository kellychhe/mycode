#!/usr/bin/python3

def main(): 
    
    # Ask the user to input their name then date and store in a variable
    # Make sure the user does not submit blank input
    name = input("Please enter your name: ")
    while name == "" :
        name = input("You did not enter a name. Please try again ")

    day = input("What day of the week is it? ")
    while day == "" :
        day = input("Answer the question plsss")

    # Use f string to print out statement using input variables
    print(f"Hello, {name}! Happy {day}!")

# Run the function    
main()
