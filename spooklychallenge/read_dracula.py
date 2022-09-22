#!/usr/bin/python3


# initialize vampire counter 
count = 0

# open the file for reading
with open("dracula.txt", "r") as dracula:
    #write a text for the vampire lines
    with open("vampire.txt", "w") as vampiredoc:
    # loop over the list of lines
        for line in dracula:
            # print each line that has the word vampire in it
            if "vampire" in line.lower():
                count += 1
                print(line)
                vampiredoc.write(line)
print("The number of lines the word vampire is in", count)


