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



def loopss(n):
    for i in range(1, n+1):
        for j in range(1,i+1):
            print(j, end=' ')
        print()

n = int(input())
loopss(n)