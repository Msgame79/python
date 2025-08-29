import os
import requests

if os.path.exists("./musics"):
    os.system("del musics /q")
os.mkdir("musics")

if not os.path.exists("./uuids.txt"):
    requests