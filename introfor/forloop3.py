#!/usr/bin/env python3
"""RZFeeser | Alta3 Research
   nesting an if-statement inside of a for loop"""

def main():
    farms = [{"name": "NE Farm", "agriculture": ["sheep", "cows", "pigs", "chickens", "llamas", "cats"]},
             {"name": "W Farm", "agriculture": ["pigs", "chickens", "llamas"]},
             {"name": "SE Farm", "agriculture": ["chickens", "carrots", "celery"]}]
    
    for farm in farms:
        print("\nThe " + farm["name"] + " is the place to be! \nThey have ")

        for agriculture in farm.get("agriculture"):
            print(agriculture, end=" "

if __name__ == "__main__":
    main()
        
