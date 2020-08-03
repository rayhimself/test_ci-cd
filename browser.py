import sys
import os
import requests
from bs4 import doc
power = True
command_list = []
direc = 'dir'
#args = sys.argv
#direc = args[1]
try:
    os.mkdir(direc)
except FileExistsError:
    pass
history =[]
while power:
    URL = input('> ')
    if URL != 'exit':
        if '.' in URL:
            name = URL.split('.')
            name.pop()
            name = '.'.join(name)
            r = requests.get('https://' + URL)
            soup = BeautifulSoup(r.text, 'html.parser')
            soup = list(soup.children)[3]
            soup = list(soup.children)
            if soup[3] == '\n':
                soup = soup[2]
            else:
                soup = soup[3]
            p = list(soup.children)[1]
            print(p)
            file = open(direc + '/' + name + '.txt', 'w', encoding='utf8')
            file.write(str(soup))
            file.close()
            history.append(soup)
        elif URL + '.txt' in os.listdir(direc):
            file = open(direc + '/' + URL + '.txt', 'r')
            text = file.read()
            print(text)
            file.close()
            history.append(text)
        elif URL == 'back':
            if command_list.pop() != 'back':
                history.pop()
                print(history.pop())
            elif len(history) != 0:
                print(history.pop())
            else:
                pass
        else:
            print('Error: No domain zone')
        command_list.append(URL)
    else:
        power = False
