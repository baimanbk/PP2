def histogram(ls):
    s = ''
    for i in range(0, len(ls)):
        for x in range(0, ls[i]):
            x = '*'
            s += x
        print(s)
histogram([3,5,6])