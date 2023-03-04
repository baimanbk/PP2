import re

def text_match(text):
    sd = '^abb$'
    ds = '^abbb$'
    if re.search(sd, text) or re.search(ds, text):
        print('Found a match')
    else:
        print('not matched')

text_match('abb')
text_match('abbb')
text_match('abbbb')
    
