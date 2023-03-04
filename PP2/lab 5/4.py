import re

def upandlow(text):
    sd = re.findall('[A-Z][a-z]+', text)
    print(sd)

upandlow('Sdass,Asd')