# a = input()
# print(a.upper())

# a = input()
# print(a.lower())

# s = input()
# print(s.lower().count('e'))

# s = input()
# print(s.replace('w', "").replace('z', ""))

# s = input()
# print(s.rfind('a'))

# s = input()
# print(int(s.count(' '))+1)
#
# print(len(s.split()))

s = input()
print(s.replace(' ', ','))

s = input()
new = s.lower().replace('a', '').replace('o', '').replace('y', '').replace('e', '').replace('u', '').replace('i', '')
print('.' + '.'.join(new))
