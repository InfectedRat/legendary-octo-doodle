# n = int(input())
# i = 2
# natlst = []
# while i <= n:
#     if n % i == 0:
#         natlst.append(i)
#     i += 1
# print(min(natlst))

# n = int(input())
# i = 2
# while True:
#     if n%i == 0:
#         print(i)
#         break
#     i+=1

# a, b = [int(input()) for _ in range(2)]
# while a<=b:
#     if a%777==0:
#         break
#     if a%2!=0 and a%3!=0:
#         print(a)
#     a+=1

a = int(input())
b = int(input())
while a<=b:
    if a%777==0:
        break
    if a%2!=0 and a%3!=0:
        print(a)
    a+=1



