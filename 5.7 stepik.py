n = int(input())
a=[]
summ=0

for i in range(n):
    a.append(list((map(int, input().split()))))

for i in range(n):
    for j in range(n):
        if a[i][0] == a[j][1]:
            summ=summ+1

print(summ)

