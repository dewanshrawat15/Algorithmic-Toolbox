# Uses python3
import sys

def gcd_naive(a, b):
    current_gcd = 1
    for d in range(2, min(a, b) + 1):
        if a % d == 0 and b % d == 0:
            if d > current_gcd:
                current_gcd = d

    return current_gcd

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

if __name__ == "__main__":
    a, b = map(int, input().split())
    print(gcd_naive(a, b))
    print(gcd(a, b))
