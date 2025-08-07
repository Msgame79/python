"""
created by Msgames79
version: 3.13.6
compiled with pyinstaller
windows用だし配布用ではない
"""

import os
import math
import random

def clear_screen():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

clear_screen()
levels = ["Mansion", "Train", "Carry", "Mountain", "Demolition", "Castle", "Water", "Power Plant", "Aztec", "Dark", "Steam", "Ice", "Reprise"]
text1=""
levelindex = random.sample(list(range(len(levels))),len(levels))

for i in range(13):
    if i <= 8:
        text1 += "0"+str(i+1)+". "+" "*(11 - len(levels[levelindex[i]]))+levels[levelindex[i]]+"\n"
    elif i <= len(levels)-2 :
        text1 += str(i+1)+". "+" "*(11 - len(levels[levelindex[i]]))+levels[levelindex[i]]+"\n"
    else:
        text1 += str(i+1)+". "+" "*(11 - len(levels[levelindex[i]]))+levels[levelindex[i]]
id = 0
temp=list(range(len(levels)))
for i in range(len(levels)):
    for j in range(len(levels)):
        if levelindex[i] == temp[j]:
            temp.pop(j)
            id += j * math.factorial(len(levels) - 1 - i)
            break


with open("C:/自分用/OBSPortable/Scripts/Randomize.txt","w",encoding="utf-8") as a:
    a.write(text1)

text2 = "categories {\nany \"Any%\" ()\ncheckpoint \"Checkpoint%\" (checkpoint)\nnocheckpoint \"No Checkpoint%\" (nocheckpoint)\njumpless \"Jumpless%\" (jumpless)\nvoiceline \"Voiceline%\" (voiceline)\nglitchless \"Glitchless%\" ()\nonearm \"One Arm%\" ()\nrandom \"Randomize%\" ()\n}\nmappacks {\nmain \"ノーマルステージ\"{\n0 \"ミュージアム\"\n1 \"トレイン\"\n2 \"オハコビ\"\n3 \"マウンテン\"\n4 \"コウジゲンバ\"\n5 \"キャッスル\"\n6 \"ウォーター\"\n7 \"ハツデンショ\"\n8 \"アステカ\"\n9 \"ダーク\"\n10 \"スチーム\"\n11 \"アイス\"\n12 \"リプライズ\"\n}\nextra \"エクストラステージ\"{\n100 \"サーマル\"\n101 \"ファクトリー\"\n102 \"ゴルフ\"\n103 \"シティ\"\n104 \"フォレスト\"\n105 \"ラボラトリー\"\n106 \"ランバー\"\n107 \"レッドロック\"\n108 \"タワー\"\n109 \"ミニチュア\"\n110 \"カッパーワールド\"\n112 \"ポート\"\n113 \"アンダーウォーター\"\n114 \"ドックヤード\"\n115 \"美術館\"\n116 \"ハイキング\"\n117 \"キャンディランド\"\n118 \"Test Chamber\"\n}"+"\nrandom \"Randomize%("+str(id)+")\" {\n"
for b in range(len(levels)):
    text2 += str(levelindex[b]) + " \"" + levels[levelindex[b]] + "\"\n"
text2 += "}\n}"
with open("../BepInEx/plugins/Timer Categories.txt","w",encoding="utf-8") as b:
    b.write(text2)