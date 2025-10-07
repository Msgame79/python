import random
import os
a=0
while(True):
    a+=1
    os.system("cls")
    daihyou = ["kottu","Msgames79"]
    members = ["kos","turu","torute","ryu","purin","iwnl","Neo","yuutaku"]
    random1 = random.sample(list(range(2)),2)
    random2 = random.sample(list(range(8)),8)
    print("team 1\n"+daihyou[random1[0]])
    for i in range(4):
        print(members[random2[i]])
    print("\nteam 2\n"+daihyou[random1[1]])
    for i in range(4):
        print(members[random2[i+4]])
    input("a:"+str(a))