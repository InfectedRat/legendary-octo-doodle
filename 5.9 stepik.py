# a = [0 for i in range(100)]
# print(len(a))

# n = int(input())
# a = [i for i in range(1, n+1)]
# print(a)

n = int(input())
a = [i for i in range(1, n+1) if n%i==0]
print(a)