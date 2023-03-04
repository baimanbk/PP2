import re

def aandb(text):
    x = 'a.*?b$'
    if re.search(x, text):
        print('Found a match')
    else:
        print('Not mached')
aandb('asdjkhfjdkhb,asdb')