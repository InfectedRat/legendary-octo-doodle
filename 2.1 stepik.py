a, b = [input() for _ in range(2)]
print(a, b, sep='\n')

a, b, c = [input() for _ in range(3)]
print(c, b, a, sep='\n')

s = input()
print(s*3)

s = input()
print(len(s))

a,b = [input() for _ in range(2)]
print(b+a)

a, b, c = map(str, input().split())
print(f'Simvol code {a} is {ord(a)}.')
print(f'Simvol code {b} is {ord(b)}.')
print(f'Simvol code {c} is {ord(c)}.')

[print(f"Simvol code {x} is {ord(x)}.") for x in input().split()]

