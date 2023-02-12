def prime_n(ls):
    ls1 = []
    for i in range(0, len(ls)):
        for x in range(2, ls[i]):
            if ls[i] == 2:
                ls1.append(ls[i])
                break
            if ls[i] % 2 != 0:
                ls1.append(ls[i])
                break
            else:
                continue
    print(ls1)
        
ls = [2, 4, 5, 6, 8, 7, 11]
prime_n(ls)