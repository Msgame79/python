import os
import random
import math

def clear_screen():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

while True:
    while True:
        try:
            clear_screen()
            a = input("Insert a positive integer:")
            if int(a) >= 1:
                break
            else:
                pass
        except ValueError:
            pass
    a = int(a)
    b = list(range(a))
    c = random.sample(b, a)
    d = list(range(a))
    e = 0

    for i in range(a):
        for j in range(a):
            if c[i] == d[j]:
                d.pop(j)
                e += j * math.factorial(a - 1 - i)
                break

    print(b)
    print(c)
    print(e)
    input()