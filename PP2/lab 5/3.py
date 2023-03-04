import re

def lowlet(text):
    sd = re.findall('[a-z]_',text)
    if sd:
        print(sd)
    else:
        print('no match')

lowlet('a_d_dfsd,s')