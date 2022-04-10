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

def summ(num):
    summ = 0
    while num > 0:
        last_num = num % 10
        summ = summ + last_num
        num = num // 10
    return summ


num = int(input())
print(summ(num))
