mas = input().split()
mas.reverse()
print(*mas)

a = list(map(int, input().split()))
print(a.count(999))

a = input().upper().split()
print('-'.join(a[0])+' '+'-'.join(a[1]))

a, b = map(str,input().split())
c = a.upper()
d = b.upper()
e = c[:]
f = d[:]
g = '-'.join(e)
h = '-'.join(f)
print(f'{g} {h}')

print("\n".join(list(input().split())))

a = input().split()
print(a.join('\n'))

a = list(input().split())
a = '\n'.join(a)
print(a)

fio = input().split()
im = fio[0]
ot = fio[1]
print(f'{fio[2]} {im[0]}.{ot[0]}.')
# print(im)
# print(ot)
