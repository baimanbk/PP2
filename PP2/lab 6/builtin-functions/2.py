import re
def upperandlower(text):
    cnt1 = 0
    cnt2 = 0
    for i in text:
        if i.isupper():
            cnt1 = cnt1 + 1
        elif i.islower():
            cnt2 = cnt2 + 1
    print(cnt1)
    print(cnt2)

upperandlower('ASDasd')