summ=0
cn=0
alls=0

for i in range(1000, 10000):
    cn = i
    summ = 0
    while cn>0:
        summ+=cn%10
        cn//=10
    if summ == 20:
        alls+=i

    print(i, summ, alls)

