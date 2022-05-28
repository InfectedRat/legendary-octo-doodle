# n = int(input())
# a=[]
# summ=0
#
# for i in range(n):
#     a.append(list((map(int, input().split()))))
#
# for i in range(n):
#     for j in range(n):
#         if a[i][0] == a[j][1]:
#             summ=summ+1
#
# print(summ)

n, m = map(int, input().split())
a=[]

for i in range(n):
    a.append(list((map(int, input().split()))))

print(a)
n, m = map(int, input().split())
a=[]

for i in range(n):
    a.append(list((map(int, input().split()))))

print(a)

# put your python code here
s = 0
a = 1
while a != 0:
    a = int(input())
    s += a
print(s)

s = 0
a = 1
while a != 0:
    a = int(input())
    s += a
print(s)