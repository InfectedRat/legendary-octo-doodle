def f(x):
    a = 0
    if x <= -2:
        a = 1 - (x + 2) ** 2
    elif -2 < x <= 2:
        a = (x / 2) * -1
    elif 2 < x:
        a = (x - 2) ** 2 + 1
    return a


print(f(4.5))
