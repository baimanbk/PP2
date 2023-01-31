n = int(input())

while(n > 1440):
    n = n - 1440
a = n // 60
b = n % 60
if(n == 1440):
    a = 0
    b = 0
print(a,b)