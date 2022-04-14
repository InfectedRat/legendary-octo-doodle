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

a, b = [int(input()) for _ in range(2)]

for i in range(a, b+1):
    if (i%3==0 and i%5==0):
        print('FizzBuzz')
    elif i%5==0:
        print('Buzz')
    elif i%3==0:
        print('Fizz')
    else:
        print(i)
