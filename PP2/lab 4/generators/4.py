def square(a,b):
    for i in range(a,b+1):
        yield i ** 2

print(*square(4,8))