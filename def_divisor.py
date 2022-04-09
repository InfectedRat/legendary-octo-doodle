def gcd(a, b):
    r = 1
    while r != 0:
        if a > b:
            r = a % b
            a = r
        else:
            r = b % a
            b = r

    if a > b:
        b = a
    else:
        b
    return b

def main():
    a, b = map(int, input().split())
    print(gcd(a, b))


if __name__ == "__main__":
    main()