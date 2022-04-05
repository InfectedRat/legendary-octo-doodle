# a, b = [int(input()) for _ in range(2)]
# if a<b:
#     print('<')
# elif a>b:
#     print('>')
# else:
#     print('=')

# a, b, c = [int(input()) for _ in range(3)]
# if c<a>b:
#     print(a)
# elif c<b>a:
#     print(b)
# else:
#     print(c)

# a = int(input())
# if a % 2 == 0:
#     print(a // 2)
# elif a == 1:
#     print(0)
# else:
#     print(a)

# a, b, c = map(int, input().split())
# mx = 0
# mi = 0
# if a>b and a>c:
#     mx=a
# elif b>a and b>c:
#     mx=b
# elif c>a and c>b:
#     mx=c
#
# if a<b and a<c:
#     mi=a
# elif b<a and b<c:
#     mi=b
# elif c<a and c<b:
#     mi=c
#
# print(mx-mi)

# s1, s2 = [str(input()) for _ in range(2)]
# if s1.lower() > s2.lower():
#     print(1)
# elif s1.lower() < s2.lower():
#     print(-1)
# else:
#     print(0)

s, v1, v2, t1, t2 = map(int, input().split())
vtxt1 = v1*s
vtxt2 = v2*s
ping1 = 2*t1
ping2 = 2*t2
tp1 = vtxt1+ping1
tp2 = vtxt2+ping2

print(tp1)
print(tp2)

if tp1 == tp2:
    print('Friendship')
elif tp1 < tp2:
    print('First')
else:
    print('Second')


