# number = 73408
# m = 0
# s = 0
# while number > 0:
#     last_digit = number % 10
#     s = s + last_digit
#     if last_digit > m:
#         m = last_digit
#     number = number // 10
# print(s + m)

# num = int(input())
# while num > 0:
#     last_num = num%10
#     print(last_num)
#     num = num//10

# def summ(num):
#     summ = 1
#     while num > 0:
#         last_num = num % 10
#         summ = summ * last_num
#         num = num // 10
#     return summ
#
#
# num = int(input())
# print(summ(num))

# dl = []
# while True:
#     dl.append(int(input()))
#     if 0 in dl:
#         break
# print(sum(dl))
def minax(num):
    minn = 9
    maxx = 0
    while num > 0:
        last_num = num % 10
        if last_num > maxx:
            maxx = last_num
        if last_num < minn:
            minn = last_num
        num = num // 10
    return minn, maxx


num = int(input())
print(*minax(num), sep='\n')
