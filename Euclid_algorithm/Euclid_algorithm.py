def gcd(a, b):
    q = a // b
    r = a - q * b
    if r == 0:
        return b
    else:
        return gcd(b, r)


print(gcd(9, 4))