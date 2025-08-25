"""
created by Msgames79
version: 3.13.5
compiled with pyinstaller
"""

import os
import math
import random

def clear_screen():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

while True:
    levels = ["Mansion","Train","Carry","Mountain","Demolition","Castle","Water","Power Plant","Aztec","Dark","Steam","Ice","Reprise"]
    # levels = ["Mansion","Train","Carry","Mountain","Demolition","Castle","Water","Power Plant","Aztec","Dark","Steam","Ice","Reprise","Thermal","Factory","Golf","City","Forest","Laboratory","Lumber","Red Rock","Tower","Miniature","Copper World","Port","Underwater","Dockyard","Museum","Hike","Candyland","Test Chamber"] # 勇気があればコメントアウト解除
    while True:
        try:
            clear_screen()
            a = input("Insert an integer between 0 and "+str(math.factorial(len(levels))-1)+" otherwise generate a mnumber:")
            if 0 <= int(a) and int(a) <= math.factorial(len(levels))-1:
                break
            else:
                pass
        except ValueError:
            a = random.randint(0,math.factorial(len(levels))-1)
            clear_screen()
            print("Insert an integer between 0 and "+str(math.factorial(len(levels))-1)+" otherwise generate a mnumber:"+str(a))
            break

    b=int(a)
    for i in range(len(levels)-1,-1,-1):
        print(levels[b//math.factorial(i)])
        levels.pop(b//math.factorial(i))
        b=b%math.factorial(i)
    input("Enter to reset")