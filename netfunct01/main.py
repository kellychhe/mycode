#!/usr/bin/env python3
"""Alta3 Research || Author: RZFeeser@alta3.com"""

# importing crayons to use color
import crayons
import json

# function to push commands
def commandpush(devicecmd): # devicecmd==dict

    for ip in devicecmd.keys(): # looping through the dict
        print(f'{crayons.red("Handshaking")}. .. ... connecting with {ip}') # fstring
        # we'll learn to write code that connects to devices here
        for mycmds in devicecmd[ip]:
            print(f'Attempting to sending command --> {mycmds}')
            # we'll learn to write code that sends cmds to device here
    return None

# function to reboot device
def devicereboot(ips):
    
    # loop through list of ips
    for ip in ips:
        # display which ips are getting connected to
        print(f"Connecting to... {ip}")
    # let the user know that they are rebooting
    print(f'crayons.green("REBOOTING NOW!")')

# start our main script
def main():
    """called at runtime"""
    
    # open and read json file
    with open("devicecmd.json", "r") as devicecmdfile:
        # convert json to python data
        devicecmd = json.load(devicecmdfile)

    # dict containing IPs mapped to a list of physical interfaces and their state
    #devicecmd = {"10.1.0.1":["interface eth1/2", "no shutdown"], "10.2.0.1":
    #["interface eth1/1", "shutdown"], "10.3.0.1":["interface eth1/5", "no shutdown"]}

    print(f"Welcome to the {crayons.blue('Network')} device command pusher") # welcome message

    ## get data set
    print("\nData set found\n") # replace with function call that reads in data from file

    ## run
    commandpush(devicecmd) # call function to push commands to devices

# call our main function
main()

