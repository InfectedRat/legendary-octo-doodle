# a = [0 for i in range(100)]
# print(len(a))

# n = int(input())
# a = [i for i in range(1, n+1)]
# print(a)

# n = int(input())
# a = [i for i in range(1, n+1) if n%i==0]
# print(a)

# n = int(input())
# a = [i for i in range(n, (n**2)+1) if i%2!=0]
# print(a)

a, b = map(int, input().split())

if a<=b:
    c = [i**2 for i in range(a, b+1)]
elif a>b:
    c = [i**3 for i in range(b, a+1)]

# print(c[::-1])

if a<=b:
    print(c)
else:
    print(c[::-1])