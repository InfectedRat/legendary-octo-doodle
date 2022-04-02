instr = input()
print('Что Вы сказали? {s}? Какое интересное слово'.format(s=instr))

name, surname = [input() for _ in range(2)]
print('Здравствуйте, {s} {n}!'.format(n=name, s=surname))

n = int(input())
a = n-1
b = n+1
print('Для числа {n} предыдущим будет число {a}.'.format(n=n, a=a))
print('Для числа {n} следующим будет число {b}.'.format(n=n, b=b))
