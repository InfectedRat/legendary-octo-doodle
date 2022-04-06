n = int(input())

if n%3==0 and n%5==0:
    print('FizzBuzz')
elif n%3==0:
    print('Fizz')
elif n%5==0:
    print('Buzz')
else:
    print(n)


a, b, c = [int(input()) for _ in range(3)]

if a == b == c:
    print(3)
elif a == b or a == c or b == c:
    print(2)
else:
    print(0)

n = int(input())

if n == 1:
    print('Январь')
elif n == 2:
    print('Февраль')
elif n == 3:
    print('Март')
elif n == 4:
    print('Апрель')
elif n == 5:
    print('Май')
elif n == 6:
    print('Июнь')
elif n == 7:
    print('Июль')
elif n == 8:
    print('Август')
elif n == 9:
    print('Сентябрь')
elif n == 10:
    print('Октябрь')
elif n == 11:
    print('Ноябрь')
else:
    print('Декабрь')

dic = dict(enumerate('Январь Февраль Март Апрель Май Июнь Июль Август Сентябрь Октябрь Ноябрь Декабрь'.split(), 1))
print(dic[int(input())])

n = int(input())
if n<2:
    print('Младенец')
elif 2<=n<4:
    print('Малыш')
elif 4<=n<12:
    print('Ребенок')
elif 12<=n<19:
    print('Подросток')
elif 19<=n<65:
    print('Взрослый человек')
elif n>=65:
    print('Пожилой человек')

a, b = [float(input()) for _ in range(2)]
op = str(input())

if op != '+' and  op != '-' and  op != '*' and op != '/':
    print('Неизвестно')
elif op == '+':
    print(a+b)
elif op == '-':
    print(a-b)
elif op == '*':
    print(a * b)
elif op == '/' and b != 0:
    print(a/b)
else:
    print('Неизвестно')

pasw = str(input())
rpasw = str(input())

if len(pasw)<7:
    print('Short')
elif pasw != rpasw:
    print('Difference')
else:
    print('OK')