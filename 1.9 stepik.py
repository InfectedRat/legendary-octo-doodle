import math

a = int(input())
print(math.ceil(a/10))

a = int(input())
print(math.ceil(a/4))

a, b, c = [int(input()) for _ in range(3)]
print(math.ceil(a/2)+math.ceil(b/2)+math.ceil(c/2))

l, w, h, = map(int, input().split())
print(math.ceil((((l+w)*2)*h)/16))
