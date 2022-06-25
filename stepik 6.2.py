d1 = {}
st = input().lower()

for i in st:
    if i.isalpha():
        if i in d1:
            d1[i] += 1
        else:
            d1[i] = 1

print(d1)

