"""
created by Msgames79
version: 3.13.5
compiled with pyinstaller
"""

import random
import os

while True:
    while True:
        try:
            os.system("cls")
            a=input("Insert an positive integer:")
            if int(a)>=1:
                break
            else:
                pass
        except ValueError:
            pass
    b=0
    while True:
        b+=1
        os.system("cls")
        bogo = random.sample(list(range(int(a))),int(a))
        print("Length:"+str(a)+"\ncount:"+str(b)+"\narray:"+str(bogo))
        if list(range(int(a)))==bogo:
            break
    os.system("cls")
    print("Length:"+str(a)+"\ncount:"+str(b)+"\narray:"+str(bogo))
    input()