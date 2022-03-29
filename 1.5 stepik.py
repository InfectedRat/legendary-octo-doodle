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

n, a, b = map(int, input().split())
result = ((a * b) * n) * 2
print(result)
