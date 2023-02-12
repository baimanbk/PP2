def unielem(ls):
    ls1 = []
    for i in ls:
        if i not in ls1:
            ls1.append(i)
    return ls1