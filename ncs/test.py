import os
import requests
import codecs

def clear_screen():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

clear_screen()

r = requests.head('https://ncs.io/track/download/8cd5db57-c4b6-4ebe-8090-eca87cbb0342')
print(codecs.decode(codecs.encode(r.headers['Content-Disposition'],'latin1')))