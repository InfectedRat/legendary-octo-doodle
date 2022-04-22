n = int(input())
a = []
summ = 0
# for i in range(n):
#     a.append([0]*n)

# for i in range(n):
#     b = []
#     for j in range(n):
#         b.append(list(map(int, input().split())))
#     a.append(b)

for i in range(n):
    a.append(list(map(int, input().split())))

for i in range(n):
    su=0
    for j in range(n):
        if i == j:
            su = a[i][j]
            summ = su+summ

# print(summ)

# for i in range(n):
#     print(a[i])

n, m = map(int, input().split())
a=[]

# for i in range(n):
#    a.append([0]*n)

for i in range(n):
    a.append(list(map(int, input().split())))

# for i in range(n):
#      print(a[i])

for i in range(n):
    for j in range(m-1, -1, -1):
        print(a[i][j], end=' ')
    print()