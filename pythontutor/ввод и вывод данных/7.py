a = int(input())
b = int(input())
c = int(input())
if(a % 2 == 1):
    d = a // 2
    d = d+1
    
else: d = a//2
if(b % 2 == 1):
    e = b // 2
    e = e+1
else: e = b // 2
if(c % 2 == 1):
    f = c // 2
    f = f+1
else: f = c //2
print(d + e + f)