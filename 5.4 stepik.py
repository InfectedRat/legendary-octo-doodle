# n = input()
# a = [0]*10
#
# for i in str(n):
#     digit = int(i)
#     a[digit]+=1
#
# for i in range(10):
#     if a[i]>0:
#         print(i, a[i])

# n = input()
# # ls = [i for i in input()]
# ls = list(map(int, input().split()))
# # print(ls)
# minnls = []
#
# for i in range(len(ls)):
#     minn = min(ls)
#     minnls.append(minn)
#     ls.remove(minn)
#
# print(*minnls)


# sadasda = int(input())
n = list(map(int,input().split()))
count = [0]*201
for i in n:
    count[i+100]+=1
print(count)
for i in range(201):
    if count[i]>0:
        print((str(i-100)+' ')*count[i], end = '')
print(count)
# print(count)
