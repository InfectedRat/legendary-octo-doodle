# a = [0 for i in range(100)]
# print(len(a))

# n = int(input())
# a = [i for i in range(1, n+1)]
# print(a)

# n = int(input())
# a = [i for i in range(1, n+1) if n%i==0]
# print(a)

# n = int(input())
# a = [i for i in range(n, (n**2)+1) if i%2!=0]
# print(a)

# a, b = map(int, input().split())
#
# if a<=b:
#     c = [i**2 for i in range(a, b+1)]
# elif a>b:
#     c = [i**3 for i in range(b, a+1)]
#
# # print(c[::-1])
#
# if a<=b:
#     print(c)
# else:
#     print(c[::-1])

# st = 'Create a list of the first letters of every word in this string'
# lst1 = st.split()
# lst2 = [lst1[i][0] for i in range(len(lst1))]
# print(lst2)

# st = 'Create a list of the first letters of every word in this string'
# st = [i[0] for i in st.split()]
# for i in st:
#     print(i, end='')

from string import ascii_uppercase

n = int(input())
ls = [i for i in ascii_uppercase]
print(ls[:n])

# print(ascii_uppercase) # выведет строку ABCDEFGHIJKLMNOPQRSTUVWXYZ
