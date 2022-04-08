# k = 10
# z = 0
# while k <= 14:
#     z = z + k
#     k += 1
# print(z)

# k = 1000
# while k<=2000:
#     print(k)
#     k=k+1

# k = 6785
# while k>=195:
#     print(k)
#     k=k-5

a, b = map(int, input().split())
k=0
while a<=b:
    a=a*3
    b=b*2
    k=k+1
print(k)