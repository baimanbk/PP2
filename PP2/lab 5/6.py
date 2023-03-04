import re

def space(text):
    x = re.sub("\s", ",", text)
    y = re.sub('\.', ':', x)
    #print(x)
    print(y)

space('asd s d.fg.sd')
#space("asd.sd.s")