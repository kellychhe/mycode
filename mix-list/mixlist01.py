#!/usr/bin/env python3

"""Learning more about lists"""

# create a three item list
my_list = [ "192.168.0.5", 5060, "UP" ]

# display first element in the list
print("The first item in the list (IP): " + my_list[0] )

# display second element in the list 
print("The second item in the list (port): " + str(my_list[1]) )

# display last element in the list
print("The last item in the list (state): " + my_list[2] )



## CHALLENGE 01

# create a list of ip information
iplist = [ 560, "80", 55, "10.0.0.1", "10.20.30.1", "ssh" ]

# display only the ip addresses in the list
print(f"The IP addresses are: {iplist[3]} and {iplist[4]}")
