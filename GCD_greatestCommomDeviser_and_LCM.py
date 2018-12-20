def gcd(a, b):
    while b > 0:
        tmp = a
        a = b
        b = tmp % b
    return a


def lcm(a, b):
    tmp = gcd(a, b)
    return (a//tmp) * b
