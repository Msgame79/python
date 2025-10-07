import os
import requests
import multiprocessing

def clear_screen():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def download(a,b):
    print(a[b])

processes = []

if __name__ == '__main__':

    clear_screen()
    if os.path.exists("./musics"):
        os.system("rd /q .\\musics")
    os.mkdir("musics")

    if os.path.exists("./log.txt"):
        os.system("del .\\log.txt /q")

    a = requests.get("https://raw.githubusercontent.com/Msgame79/python/refs/heads/main/ncs/uuids.txt")
    b = a.text.splitlines()
    for i in range(len(b)):
        p = multiprocessing.Process(target=download, args=(b,i))
        processes.append(p)
        p.start()

    for p in processes:
        p.join()