import re

def text_match(text):
    sd = '^a(b*)$'
    if re.search(sd, text):
        return 'Found a match'
    else:
        return 'not matched' 

print(text_match("ab"))