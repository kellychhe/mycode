#!/usr/bin/env python3


import netifaces




def main():
    
    print(netifaces.interfaces())

    for i in netifaces.interfaces():
        print('\n**************Details of Interface - ' + i + ' *********************')
        try:
            print('MAC: ', end='')
            # Prints the MAC address
            print(netifaces.ifaddresses(i)[netifaces.AF_LINK][0]['addr'])
            print('IP: ', end='')
            # Prints the IP address
            print(netifaces.ifaddresses(i)[netifaces.AF_INET][0]['addr'])
        except:
            # Print an error message
            print('Could not collect adapter information')

if __name__ == "__main__":
    main()
