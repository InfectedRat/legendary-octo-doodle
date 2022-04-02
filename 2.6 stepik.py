# instr = input()
# print('Что Вы сказали? {s}? Какое интересное слово'.format(s=instr))

name, surname = [input() for _ in range(2)]
print('Здравствуйте, {s} {n}!'.format(n=name, s=surname))
