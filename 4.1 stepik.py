k = 10
z = 0
while k <= 14:
    z = z + k
    k += 1
print(z)

k = 1000
while k<=2000:
    print(k)
    k=k+1

k = 6785
while k>=195:
    print(k)
    k=k-5

a, b = map(int, input().split())
k=0
while a<=b:
    a=a*3
    b=b*2
    k=k+1
print(k)

numbers = [2, 3, 7, 9, 5, 0, 6, 3, 6, 0, 1, 7, 9, 4, 4, 4, 2, 2, 6, 9, 1, 7, 0, 3, 8, 1, 0, 3, 8, 0, 8, 4, 0, 2, 3, 6, 6,
           1, 5, 8, 7, 2, 3, 8, 7, 7, 1, 2, 2, 8, 4, 3, 4, 8, 0, 7, 9, 8, 3, 7, 7, 7, 7, 5, 1, 7, 4, 5, 0, 8, 0, 9, 2, 4,
           7, 6, 6, 5, 9, 7, 1, 7, 8, 8, 3, 4, 9, 7, 6, 4, 2, 0, 0, 0, 9, 4, 0, 9, 4, 4, 4, 5, 5, 4, 2, 5, 9, 4, 8, 1, 5,
           7, 1, 0, 2, 6, 8, 7, 2, 7, 9, 3, 6, 4, 7, 5, 0, 7, 2, 0, 8, 2, 9, 8, 6, 4, 4, 7, 5, 5, 9, 4, 9, 5, 6, 9, 1, 1,
           3, 1, 5, 2, 1, 7, 0, 0, 7, 8, 1, 3, 0, 0, 4, 4, 3, 3, 6, 7, 8, 6, 1, 2, 0, 2, 0, 9, 9, 0, 5, 2, 4, 1, 7, 4, 9,
           9, 4, 9, 6, 9, 2, 7, 1, 2, 4, 5, 4, 0, 9, 0]

while 4 in numbers:
    numbers.remove(4)
print(*numbers)

s = input()
print(s)
while len(s)>0:
    s = s[1:-1]
    print(s)


import math
print(math.sqrt(15))

k = int(input())
n = 1
g = 0
while n <= k:
    print(n)
    g = g+1
    n = (g + 1) ** 2

def sport(x, y):
    k = 1
    while x <= y:
        k += 1
        x = x * 1.15
    return k


x, y = map(int, input().split())
print(sport(x, y))


def ebanyi_vasya(n, m):
    d = 0
    i = 1
    while n > 0:
        n = n - 1
        d = d + 1
        if d == m * i:
            n = n + 1
            i = i + 1
    return d


n, m = map(int, input().split())
print(ebanyi_vasya(n, m))

def ebanaya_stepen(n):
    i = 0
    while n >= 2:
        n = n - 2 ** i
        i += 1

    if n == 1:
        return i
    else:
        return 'НЕТ'


n = int(input())
print(ebanaya_stepen(n))

def ebanaya_edinica(n):
    fn = str(n[0])
    while int(fn[0]) != 1 and int(n) <= 10 ** 9:
        n = str(int(n) * int(fn))
        fn = str(n[0])
    return n


n = input()
print(ebanaya_edinica(n))
