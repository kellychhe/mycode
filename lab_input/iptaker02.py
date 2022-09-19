#!/usr/bin/env python3
"""Alta3 Research | RZFeeser
    print() - contcatenate vs print a series of items"""

def main():

    # collect string input form the user
    user_input = input("Please enter an IPv4 IP address:")

    ## the line below creates a singel string that is passed to print()
    # print ("You told me the IPv4 address is: ' + user_input)

    ## print() can be given a series of objects separated by a comma
    print("You told me the IPv4 address is:", user_input)

    ## collect another string inmput from user
    user_vendor = input("Please enter the vendor name associated with the device:")

    ## print the new information
    print("You told me the vendor name is:", user_vendor)

main()
