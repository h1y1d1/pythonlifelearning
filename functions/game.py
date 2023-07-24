"""
I have a dice with numbers from 1 - 6
if my total number is equal to 20..Win
if my total is > 20 lost.
random - library
"""

import random

def roll():
    return random.randint(1,6)

def game():
    total=0
    while total<20:
        current_roll = roll()
        print("roll total is:",current_roll)
        total = total+current_roll
        print("total value is:",total)
        if total==20:
            print("congratulations")
            break
        elif total<20:
            pass
        else:
            print("better luck next time")

venkat=game()



