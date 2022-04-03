salary = int(input())
if salary < 20000:
    print(salary)
else:
    print(salary-(salary*13/100))

s = input()
if s == 'Python':
    print('ДА')
else:
    print('НЕТ')

print(('НЕТ', 'ДА')[input() == 'Python'])

print("ДА" if input() == "Python" else "НЕТ")

a,b = [int(input()) for _ in range(2)]
if a>=b:
    print(a)
else:
    print(b)

print(a,b)

ispolyndr = str(int(input()))
# print(ispolyndr[::-1])
if ispolyndr[::] == ispolyndr[::-1]:
    print('YES')
else:
    print('NO')

a = int(input())
if a // 1000 == a % 10 and a % 1000 // 100 == a % 100 // 10:
    print("YES")
else:
    print("NO")

a = input()
print('YNEOS'[a != a[::-1]::2])

a, b, c = map(int, input().split())
if a+b == c:
    print('YES')
else:
    print('NO')

a, b = [input() for _ in range(2)]
# print(b[::])
# print(a[::-1])

if b[::] == a[::-1]:
    print('YES')
else:
    print('NO')

a, b, c = [int(input()) for _ in range(3)]
if a + b > c and a + c > b and b + c > a:
    print('YES')
else:
    print('NO')

ticket = int(input())
a = [ticket // 100000, ticket // 10000 % 10, ticket // 1000 % 10, ticket // 100 % 10, ticket // 10 % 10, ticket % 10]
print('YES' if a[0]+a[1]+a[2] == a[3]+a[4]+a[5] else 'NO')

a = input().rjust(6, '0')
print(a)

a = input().rjust(6,'0')
if int(a[0])+int(a[1])+int(a[2])==int(a[3])+int(a[4])+int(a[5]):
    print('YES')
else:
    print('NO')