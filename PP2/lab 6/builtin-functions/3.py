def palindrom(text):
    text1 = text[::-1]
    if text1 == text:
        print('palindrom')
    else:
        print('not palindrom')

palindrom('asd')
palindrom('asa')