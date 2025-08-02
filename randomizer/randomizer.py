"""
created by Msgames79
version: 3.13.5
compiled with pyinstaller
"""

import random
import os

levels = ["Mansion", "Train", "Carry", "Mountain", "Demolition", "Castle", "Water", "Power Plant", "Aztec", "Dark", "Steam", "Ice", "Reprise"]
text=""
levelindex = random.sample(list(range(len(levels))),len(levels))

for i in range(13):
    if i <= 8:
        text += str(i+1)+" : "+levels[levelindex[i]]+"\n"
    elif i <= len(levels)-2 :
        text += str(i+1)+": "+levels[levelindex[i]]+"\n"
    else:
        text += str(i+1)+": "+levels[levelindex[i]]

try:
    os.remove("./ForOBS.txt")
except FileNotFoundError:
    pass
with open("./ForOBS.txt","w",encoding="utf-8") as a:
    a.write(text)
    a.close()

try:
    os.remove("./Timer categories.txt")
except FileNotFoundError:
    pass

if not os.path.exists("./original.txt"):
    text1  = """categories {
any "Any%" ()
checkpoint "Checkpoint%" (checkpoint)
nocheckpoint "No Checkpoint%" (nocheckpoint)
jumpless "Jumpless%" (jumpless)
voiceline "Voiceline%" (voiceline)
glitchless "Glitchless%" ()
onearm "One Arm%" ()
random "Randomize%" ()
}
mappacks {
main "ノーマルステージ"{
0 "ミュージアム"
1 "トレイン"
2 "オハコビ"
3 "マウンテン"
4 "コウジゲンバ"
5 "キャッスル"
6 "ウォーター"
7 "ハツデンショ"
8 "アステカ"
9 "ダーク"
10 "スチーム"
11 "アイス"
12 "リプライズ"
}
extra "エクストラステージ"{
100 "サーマル"
101 "ファクトリー"
102 "ゴルフ"
103 "シティ"
104 "フォレスト"
105 "ラボラトリー"
106 "ランバー"
107 "レッドロック"
108 "タワー"
109 "ミニチュア"
110 "カッパーワールド"
112 "ポート"
113 "アンダーウォーター"
114 "ドックヤード"
115 "美術館"
116 "ハイキング"
117 "キャンディランド"
118 "Test Chamber"
}"""
else:
    with open("./original.txt","r",encoding="utf-8") as original:
        text1 = original.read()
        original.close()

text1 += "random \"Randomize%\" {\n"
for b in range(len(levels)):
    text1 += str(levelindex[b]) + " \"" + levels[levelindex[b]] + "\"\n"
text1 += "}\n}"

with open("./Timer Categories.txt","w",encoding="utf-8") as c:
    c.write(text1)
    c.close()
print("Finished successfully.\nEnter to exit.")
input()