# Uses python3
import sys

def gcd(a, b):
    if a == b:
        return a
    if a == 0:
        return b
    if b == 0:
        return a
    if (~a & 1) == 1:
        if (b & 1) == 1:
            return gcd(a >> 1, b)
        else:
            return (gcd(a >> 1, b >> 1) << 1)
    if (~b & 1) == 1:
        return gcd(a, b >> 1)
    if a > b:
        return gcd((a - b) >> 1, b)
    return gcd((b - a) >> 1, a)

def lcm_naive(a, b):
    for l in range(1, a*b + 1):
        if l % a == 0 and l % b == 0:
            return l

    return a*b

def lcm(a, b):
    return int((a * b) / gcd(a, b))

if __name__ == '__main__':
    a, b = map(int, input().split())
    # print(lcm_naive(a, b))
    print(lcm(a, b))

