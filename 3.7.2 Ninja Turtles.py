# coord = {'север': 10, 'запад': 20, 'юг': 30, 'восток': 40}
# result = set()
#
# commands_sum = {'север': 0, 'юг': 0,
#                 'запад': 0, 'восток': 0}
#
# for command, value in [input().split() for _ in range(int(input()))]:
#     commands_sum[command] += int(value)
#
# print(commands_sum['восток'] - commands_sum['запад'],
#       commands_sum['север'] - commands_sum['юг'])


# n = int(input())
a = {'север':[40,60], 'запад':[30,70], 'юг':[10,20], 'восток':[80,90]}

print(a['север'][1])

# for i in range(n):
#     i = input().split()
#     if i[0] == 'север':
#         a['север'][1] += int(i[1])
#     elif i[0] == 'запад':
#         a['запад'][0] += int(i[1])
#     elif i[0] == 'юг':
#         a['юг'][1] += int(i[1])
#     elif i[0] == 'восток':
#         a['восток'][0] += int(i[1])
#     #else:
#         #print('Ошибка ввода данных')
# print(int(a['восток'][0]) - int(a['запад'][0]), end=' ')
# print(int(a['север'][1]) - int(a['юг'][1]))

