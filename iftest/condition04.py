#!/usr/bin/env python3
"""learning how to use conditonals"""

def main():
    # ask the user for a hostname and store in variable
    hostname = input("What value should we set for hostname?")
    
    ## Notice how the next line has changed
    ## here we use the str.lower() method to return a lowercase string
    if hostname.lower() == "mtg":
        print("The hostname was found to be mtg")
        print("Hostname matches expected config")

    # print that the user is exiting at the end 
    print("Exiting the script")

# run main function
if __name__ == "__main__":
    main()
