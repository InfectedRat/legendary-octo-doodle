buklet = {}
origin_alph = input()
origin_list = [x for x in origin_alph]

cipher = input()
cipher_list = [x for x in cipher]

for_cipher = input()
for_cipher_list = [x for x in for_cipher]

for i in range(0, len(origin_list)):
    buklet[origin_list[i]] = cipher_list[i]  # словарь шифровки

for i, j in enumerate(for_cipher_list):
    for_cipher_list[i] = buklet.get(j)

# un_cipher = input()

print(origin_alph)
print(origin_list)

print(cipher)
print(cipher_list)

print(for_cipher_list)
print(buklet)
print(""".join(filter(None, for_cipher_list)))

# buklet_code = {}
# buklet_encode = {}
#
# origin_alph = input()
# cipher = input()
# for_cipher = input()
# un_cipher = input()
