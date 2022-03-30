print(*[a, b, c for a, b, c in [map(int, input().split()]])
print(*[x, y, z for x, y, z in [map(int, input().split())]])

print(4249+4247+4247+4247)

a, b, c, = map(int, input().split())
print(a, b, c, sep=',')

print(*input().split(), sep=',')

a = int(input())
print("%s<%s<%s" % (a - 1, a, a + 1))

a, b, c = [input() for _ in range(0,3)]
print(a, b, c, sep='---')

separator = input()
print(1, 2, 3, 4, 5, sep=separator)

print('Гвидо', 'Ван', 'Россум', sep='*', end='-')
print('Основатель', 'Питона', sep='_', end='!')
