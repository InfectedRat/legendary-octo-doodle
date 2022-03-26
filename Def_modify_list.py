l = [1, 2, 3, 4, 5, 6]


def modify_list(l):
    for i in (l[:]):
        if (i % 2 == 0):
            l.append(i // 2)
        l.remove(i)


print(modify_list(l))
print(l)
