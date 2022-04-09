a, b = map(int, input().split())
r = 1
while r != 0:
    if a>b:
        r=a%b
        a=r
    else:
        r=b%a
        b=r

print(a, b)

if a>b:
    b=a
else:
    b

print(b)