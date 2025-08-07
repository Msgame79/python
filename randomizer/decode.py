"""
created by Msgames79
version: 3.13.5
compiled with pyinstaller
"""

import os
import math

def clear_screen():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

while True:
    levels = ["Mansion", "Train", "Carry", "Mountain", "Demolition", "Castle", "Water", "Power Plant", "Aztec", "Dark", "Steam", "Ice", "Reprise"]
    while True:
        try:
            clear_screen()
            a = input("Insert a positive integer:")
            if int(a) >= 1 and int(a) <= math.factorial(13):
                break
            else:
                pass
        except ValueError:
            pass

    b=int(a)
    for i in range(len(levels)-1,-1,-1):
        print(levels[b//math.factorial(i)])
        levels.pop(b//math.factorial(i))
        b=b%math.factorial(i)
    input("Enter to reset")