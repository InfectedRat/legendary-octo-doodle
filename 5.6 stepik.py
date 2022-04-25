# n = int(input())
# a = []
# summ = 0
# for i in range(n):
#     a.append([0]*n)

# for i in range(n):
#     b = []
#     for j in range(n):
#         b.append(list(map(int, input().split())))
#     a.append(b)

# for i in range(n):
#     a.append(list(map(int, input().split())))
#
# for i in range(n):
#     su=0
#     for j in range(n):
#         if i == j:
#             su = a[i][j]
#             summ = su+summ

# print(summ)

# for i in range(n):
#     print(a[i])

# n, m = map(int, input().split())
# a=[]
#
# # for i in range(n):
# #    a.append([0]*n)
#
# for i in range(n):
#     a.append(list(map(int, input().split())))
#
# # for i in range(n):
# #      print(a[i])
#
# for i in range(n-1, -1, -1):
#     for j in range(m):
#         print(a[i][j], end=' ')
#     print()
#
#

# mas = []
#
# for i in range(5):
#     mas.append(list(map(int, input().split())))
#
# for i in range(5):
#     for j in range(5):
#         if mas[i][j] == 1:
#             row = i
#             column = j
# print(abs(2 - row) + abs(2 - column))

# n, m = map(int, input().split())
# a=[]
#
# for i in range(n):
#     a.append(list(map(int, input().split())))
#
# for i in range(n):
#     summ=0
#     for j in range(m):
#         summ=a[i][j]+summ
#     print(summ, end=' ')
# print()
#
# for j in range(m):
#     summ=0
#     for i in range(n):
#         summ=a[i][j]+summ
#     print(summ, end=' ')
#

# n = int(input())
# a=[]
# summ1=0
# summ2=0
#
# for i in range(n):
#     a.append(list(map(int, input().split())))
#
# for i in range(n):
#     for j in range(n):
#         if i<j:
#             summ1=a[i][j]+summ1
#
# for i in range(n):
#     for j in range(n):
#         if i>j:
#             summ2=a[i][j]+summ2
#
# print('Yes' if summ1==summ2 else 'No')

n, m = map(int, input().split())
a = []
c = []
for i in range(n):
    a.append(list(map(int, input().split())))
for i in range(n):
    s = 0
    for j in range(m):
        s += a[i][j]
    c.append(s)
print(max(c))
ind = c.index(max(c))
print(ind)

