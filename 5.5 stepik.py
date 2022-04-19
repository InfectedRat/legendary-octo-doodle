# summ=0
# cn=0
# alls=0
#
# for i in range(1000, 10000):
#     cn = i
#     summ = 0
#     while cn>0:
#         summ+=cn%10
#         cn//=10
#     if summ == 20:
#         alls+=i
#
#     print(i, summ, alls)
#

# def loopss(n):
#     for i in range(1, n+1):
#         for j in range(1,i+1):
#             print(j, end=' ')
#         print()
#
# n = int(input())
# loopss(n)

# n=int(input())
# count=0
# for p in range(n+1,2*n):
#     if p%2==0 and p!=2 or p==1:
#         continue
#     d=3
#     is_plain=True
#     while d*d<=p:
#         if p%d==0:
#             is_plain=False
#             break
#         d+=2
#     if is_plain:
#         count+=1
# print(count)

# ls = input().split()
#
# for i in ls:
#     for j in range(1, int(i)+1):
#         print('*', end='')
#     print()

# n = int(input())
# ls = input().split()
# cnt=0
# for j in range(n-1):
#     for i in range(n-1-j):
#         if ls[i]>ls[i+1]:
#             ls[i],ls[i+1]=ls[i+1],ls[i]
#             cnt+=1
# print(*ls)
# print(cnt)

n = input()
# ls = [i for i in input()]
ls = list(map(int, input().split()))
# print(ls)
minnls = []

for i in range(len(ls)):
    minn = min(ls)
    minnls.append(minn)
    ls.remove(minn)

print(*minnls)
