#!/usr/bin/env python3

"""function returns if a file is a zip file or not"""

# import zipfile for use in main
import zipfile

def main():

    # ask user which file to check
    maybezip = input("Which file do you want to check(if it is a zipfile)? ")

    # use coniditonal and zipfile import to check if file is a zip
    if zipfile.is_zipfile(maybezip):
        print("Yes, this is a zip")
    else:
        print("No this is not a zip")

if __name__ == "__main__":
    main()
