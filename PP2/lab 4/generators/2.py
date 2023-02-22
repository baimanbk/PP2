def even(n = int(input())):
    for i in range(0,n):
        if i % 2 == 0:
            print(i, end = ',')
even()