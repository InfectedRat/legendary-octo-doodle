# n = int(input())
#
# for i in range(1, n+1):
#     print(i)
#

# print(list(range(19,0,-1)))

# def type_interval(n):
#     for i in range(n,0,-1):
#         print(i)
#
# n = int(input())
# type_interval(n)

# [print('Надо было брать биткоин в 2012!') for i in range(13)]

# print([i if not i % 2 else '*' for a in range(51) for i in range(a) if a > 22])

# def bartphrase(phrase, n):
#     for i in range(n):
#         print(phrase)
#
# phrase = input()
# n = int(input())
#
# bartphrase(phrase, n)

# a, b = [int(input()) for _ in range(2)]
#
# for i in range(a, b+1):
#     if (i%3==0 and i%5==0):
#         print('FizzBuzz')
#     elif i%5==0:
#         print('Buzz')
#     elif i%3==0:
#         print('Fizz')
#     else:
#         print(i)


# def numkvadrokub(a, b):
#     for i in range(a, b + 1):
#         print(f'Число {i}; его квадрат = {i ** 2}; его куб = {i ** 3}')
#
#
# a, b = [int(input()) for _ in range(2)]
# numkvadrokub(a, b)


# n = int(input())
# mishka=0
# chris=0
#
# for i in range(n):
#     a, b = map(int, input().split())
#     if a>b:
#         mishka+=1
#     elif a<b:
#         chris+=1
# if mishka>chris:
#     print('Mishka')
# elif mishka<chris:
#     print('Chris')
# else:
#     print('Friendship is magic!^^')

# n = int(input())
# ls = []
#
# for i in range(1, n+1):
#     s = input().lower()
#     if 'рок' in s:
#         # print(i, s.find('рок')+1)
#         ls.append([i, s.find('рок')+1])
# for i in range(len(ls)):
#     print(*ls[i])

# n=int(input())
# rec_lst = []
#
# for i in range(n):
#     recept = input().lower()
#     if 'соль' not in recept:
#         rec_lst.append(recept)
# print(*rec_lst, sep=', ')

# my_str = 'barbarian'
# print(my_str.find('bar'))  # 0
# print(my_str.find('bar', 1))  # 3
# print(my_str.find('bar', 1, 2))  # -1

# n = int(input())
# summ = 0
#
# for i in range(n - 1, 1, -1):
#     if i % 3 == 0 or i % 5 == 0:
#         summ += i
#
# print(summ)


# summ = 0
#
# for i in range(50, 101):
#     summ=summ+i**3
#
# print(summ)




