#!/usr/bin/env python3

"""Using shutil and os to move files in python"""

# import tools needed to move files
import shutil   # shell utilities will be used to move files
import os       # provides access to low level of operations (regardless of type of OS)

def main():

    # move into this working directory
    os.chdir('/home/student/mycode/')

    # move file raynor.obj into ceph_storage directory
    shutil.move('raynor.obj', 'ceph_storage/')

    # ask user for a name to rename kerrigan.obj file and store in variable to use later
    xname = input('What is the new name for kerrigan.obj? ')

    # rename my moving file to same folder but with new input name
    shutil.move('ceph_storage/kerrigan.obj', 'ceph_storage/' + xname)

#run main function
if __name__ == "__main__":
    main()
