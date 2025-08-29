import random
import os

def clear_screen():
    if os.name == ('nt'):
        os.system("cls")
    else:
        os.system("clear")

while True:
    while True:
        clear_screen()
        goal = input("Enter an integer to set your destination(1-100): ")
        try:
            if 1 <= int(goal) and int(goal) <= 100:
                break
            else:
                pass
        except ValueError:
            pass

    current = 0
    presses = 0
    resets = 0
    a = 1
    for i in range(int(goal)):
        a *= (100-i)/100
    print(str(a*100)+"% chance to get "+str(goal))
    while True:
        presses += 1
        if random.randint(1,100) <= 100-current:
            current += 1
        else:
            resets += 1
            current = 0
        if current == int(goal):
            break

    print("Total presses: "+str(presses)+"\nTotal resets: "+str(resets)+"\nEnter to restart")
    input()