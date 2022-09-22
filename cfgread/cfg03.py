#!/usr/bin/env python3

## ask user what file to load
cfgfile = input("choose a file to load")

## initiate counter
counter = 0

## create file object in "r"ead mode
with open(cfgfile, "r") as configfile:
    ## readlines() creates a list by reading target
    ## file line by line
    configlist = configfile.readlines()
    counter += 1

## file was just auto closed (no more indenting)

## print the line count
print(counter)
## each item of the list now has the "\n" characters back
print(configlist)

