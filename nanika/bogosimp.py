"""
created by Msgames79
version: 3.13.5
compiled with pyinstaller
"""

import random
import os
import time

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
    c=time.time()
    while True:
        b+=1
        if list(range(int(a)))==random.sample(list(range(int(a))),int(a)):
            break
    d=time.time()-c
    os.system("cls")
    print("Length:"+str(a)+"\ncount:"+str(b)+"\ntime:"+str(d))
    input()