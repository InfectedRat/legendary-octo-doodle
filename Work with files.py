# with open('text.txt')


# s = input()
# ns = ''
# i = 0
# j = 1
# while i < (len(s) - 1):
#     if s[i] == s[i + 1]:
#         j += 1
#     else:
#         ns = ns + s[i] + str(j)
#         j = 1
#     i += 1
# print(ns + s[i] + str(j))


# s = 't13A19w10v2t10B3O17m12o16F10i11g7p19y1r13Q12D8N18X12K13x13s13O17G9n15e5D14P11o13r13S18W9J1P3O14f3K5w5G4'
# print(s)
# i = 0
# while i < (len(s)):
#     q = s[i].isalpha()
#     if not q:
#         print(q)
#         print(s[i+1])
#     # else:
#     #     print(q)
#     # print(s[i])
#     i += 1

with open('D:\dataset_3363_2.txt') as t:
    s = t.readline().strip()

def rep(symbol, iter): return symbol * int(iter)


i = 0
while i < len(s):
    iter = ''
    if s[i].isalpha():
        symbol = s[i]
        i += 1
        while s[i].isdigit():
            iter += s[i]
            if i == len(s) - 1: break
            i += 1
        print(rep(symbol, iter), end='')
