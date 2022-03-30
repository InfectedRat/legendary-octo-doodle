n, k = [int(input()) for _ in range(2)]
print(k//n)

n, r = [int(input()) for _ in range(2)]
print(n//r)

print(int(input())%10)
print(int(input())//100%10)

a = int(input())
print(a//100+a//10%10+a%10)

a = int(input())
print(a // 100 + a % 100 // 20 + a % 20 // 10 + a % 10 // 5 + a % 5)

n = int(input())
print(str(n//60//60%24), str(n//60//60+n%10))

n=int(input())
print(n+2-n%2)

a=int(input())
h=a//3600
md=((a%3600)//60)//10
m=((a%3600)//60)%10
sd=((a%3600)%60)//10
s=((a%3600)%60)%10
h=str(h)
md=str(md)
m=str(m)
sd=str(sd)
s=str(s)
print(h,md+m,sd+s,sep=':')