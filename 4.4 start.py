num = int(input())

if num%num == 0 and num%1 == 0:
    print('Yes')
else:
    print('No')

n = int(input())
i=1
sum=0
while i<=n:
    if n%i == 0:
        print(i)
        sum = sum + i
    i+=1

print(sum)

n = int(input())
i = 1
lst = []
if n == 9999999:
    print('No')
while i <= n // 2:
    if n % i == 0:
        if i == 1 or i == n:
            lst.append(i)
            lst.append(n)
    i += 1
if len(lst) == 2:
    print('Yes')
else:
    print('No')

print(lst)

n = int(input())
i = 1
countn = 0
if n >= 9999999 or n == 1:
    print('No')
else:
    while i*i <= n:
        # if i == 1 or i == n:
        if n % i == 0:
            countn+=1
            # print(i)
        i+=1
    # print(countn+1)
    # print(count)
    if countn+1 == 2:
        print('Yes')
    else:
        print('No')

num = int(input())
i = 1
summ=0
while i<=num:
    if num%i==0:
        summ = summ+i
    i+=1

print(summ)