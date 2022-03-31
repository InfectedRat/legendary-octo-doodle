a = int(input())
print(a>0)

a = int(input())
print(a%2 == 0)

a = int(input())
print(a%10 == 2)

a, b = map(int, input().split())
print(a%7 ==0 and b%7 == 0)

a,b,c = map(int,input().split())
print(a==b==c)

a = int(input())
print(5<a<=19)

a, b = [input() for _ in range(2)]
print(a == 'awesome' or b == 'awesome')

a, b, c = map(int, input().split())
print(a == b or a == c or c == b)

a = int(input())
print(9<a<100)

a, b, c = map(int, input().split())
print(a ** 2 == b ** 2 + c ** 2 or b ** 2 == a ** 2 + c ** 2 or b ** 2 == a ** 2 + c ** 2)

a, b, c = map(int, input().split())
print(a * a + b * b == c * c or a * a + c * c == b * b or b * b + c * c == a * a)
