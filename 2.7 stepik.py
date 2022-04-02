s = input()
print(f'Мое имя {s}!')

n, a = [input() for _ in range(2)]
print(f'Hello {n.upper()}. You are {a} years old.')

n, a = [input() for _ in range(2)]
print(f'{n}, вам исполнится 77 лет в {int(a) + 77}')

sec = int(input())
print(f'{sec} сек - это {sec // 60} мин. {sec % 60} сек.')

a, b = map(int, input().split())
print(f'Разрешение экрана: {a} x {b}.')
print(f'Общее количество пикселей = {a*b}.')

a, b = [int(input()) for _ in range(2)]
print(f'{a} / {b} = {a/b}\n{a} // {b} = {a//b}\n{a} % {b} = {a%b}')

a, b, c = [int(input()) for _ in range(3)]
print(f'Vector A({a}, {b}, {c})')
print(f'Vector B({a+5}, {b+5}, {c+5})')

a, b = [float(input()), int(input())]
print(f'''Current dollar rate is {a}. You want buy {b} dollars
You must pay {a * b}''')

