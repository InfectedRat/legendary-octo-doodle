# n = int(input())
# i = 2
# natlst = []
# while i <= n:
#     if n % i == 0:
#         natlst.append(i)
#     i += 1
# print(min(natlst))

# n = int(input())
# i = 2
# while True:
#     if n%i == 0:
#         print(i)
#         break
#     i+=1

# a, b = [int(input()) for _ in range(2)]
# while a<=b:
#     if a%777==0:
#         break
#     if a%2!=0 and a%3!=0:
#         print(a)
#     a+=1

# a = int(input())
# b = int(input())
# while a<=b:
#     if a%777==0:
#         break
#     if a%2!=0 and a%3!=0:
#         print(a)
#     a+=1

def nhalf(n):
    n=n/2
    return n

def n3pro(n):
    n=3*n+1
    return n

def sirakuza(n):
    cnt=0
    while True:
        if n%2==0:
            n=nhalf(n)
        else:
            n=n3pro(n)
        cnt+=1
        print(n)
        if n==1:
            break
    return cnt

def main():
    n = int(input())
    print(sirakuza(n))

if __name__ == "__main__":
    main()