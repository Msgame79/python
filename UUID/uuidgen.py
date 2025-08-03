"""
created by Msgames79
version: 3.13.5
compiled with pyinstaller
"""

import uuid
import os
a=0

while True:
    a+=1
    list = []
    now = str(uuid.uuid4())
    os.system("cls")
    print("uuid "+str(a)+":"+now)
    if now in list:
        break
    list.append(now)

print(now + " is duplicated")