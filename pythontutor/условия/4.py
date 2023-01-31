a = int(input())
if a % 400 == 0:
    print("YES")
elif a % 100 == 0:
    print("NO")
elif a % 4 == 0:
    print("YES")
else:
    print("NO")