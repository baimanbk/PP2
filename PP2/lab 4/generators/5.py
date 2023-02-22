def gen(n):
    i=0
    while n>i:
        yield n
        n=n-1

for i in gen(int(input())):
    print(i)