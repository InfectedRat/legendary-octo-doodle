# age = int(input())
# print(age+1)

# a, b = map(int, input().split())
# c = a + b
# print(c)

# s = int(input())
# s1 = s / 6
# s2 = s1 * 4
# print(int(s1), int(s2), int(s1))

# x, y, z = map(int, input().split())
# xp = 3
# yp = xp + 2
# zp = yp + 7
# print(x*xp + y*yp + z*zp)

# print(*[3 * x + 5 * y + 12 * z for x, y, z in [map(int, input().split())]])

# n, a, b = map(int, input().split())
# result = ((a * b) * n) * 2
# print(result)

# print(*[(a + b + c + d) / 4 for a, b, c, d in [map(int, input().split())]])

# a = int(input())
# b = int(input())
# c = int(input())
# x = int(input())
# y = int(input())
# z = int(input())

# a, b, c, x, y, z = [int(input()) for _ in range(6)]
# print(abs((a * 3600 + b * 60 + c) - (x * 3600 + y * 60 + z)))

# a, b = map(int, input().split())
# c = a + b
# a = c - 1 - a
# b = c - 1 - b
# print(a, b)

a, b = [int(input()) for _ in range(2)]
c = abs(a) + abs(b)
print(c)
