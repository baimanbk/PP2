def squares(end_point):
    current = 1
    while(current ** 2 <= end_point):
        yield current ** 2
        current += 1

print(*squares(16))