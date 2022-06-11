# my_dict = {}
# n = int(input())
#
# for i in range(1, n+1):
#     my_dict[i] = i * i
#
# print(my_dict)

# from string import ascii_lowercase
# # print(len(ascii_lowercase))
#
# alphabet = {}
# n=26
#
# for i in range(n):
#     alphabet[ascii_lowercase[i]] = i+1
#
# for i, j in alphabet.items():
#     print(i, j)
#
# print(alphabet)

d1 = {'a': 100, 'b': 200, 'c': 333}
d2 = {'x': 300, 'y': 200, 'z': 777}

rez = d1.copy()
rez.update(d2)

print(rez)

print(rez)