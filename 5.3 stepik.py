n = int(input())
ls = []

for i in range(n):
    s=input()
    ls.append(s)

print(ls)

s = input()
sr = input()
ls = []
ls2 = []

for i in sr.split():
    ls.append(i)

for i in ls:
    if s in i:
        ls2.append(i)

print(*ls2, sep='\n')

ls = [int(_) for _ in input().split()]
minn = max(ls)
cnt = 0

for i in ls:
    if i > 0 and i < minn:
        minn = i
        cnt+=1
if cnt>0:
    print(minn)
else:
    print('Empty')

s = input().lower()
d = 0
cnt = 0

for i in s:
    d = s.count(i)
    if d>cnt:
        cnt=d

print(cnt)


print(s[::2], s[1::2])

summ = 0
cnt = 0
s = input()

for i in s:
    if i.isdigit() == True:
        cnt += 1
        summ += int(i)

print(cnt, summ)

s = input()
for i in range(len(s)):
    s = s.replace('()', '').replace('[]', '').replace('{}', '')
if len(s) == 0:
    print('YES')
else:
    print('NO')