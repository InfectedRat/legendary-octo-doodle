str = input().lower()
lst = str.split()
d = {}

for el in lst:
    a = lst.count(el)
    d[el] = a
    # print(el, lst.count(el))

for key, value in d.items():
    print(key, value)


# print('это словарь', d)
# print(*d.items(), sep='\n')
# print(lst.count("ss"))
# print(str)
# print(lst)
