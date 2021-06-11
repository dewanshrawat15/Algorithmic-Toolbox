# Uses python3
import sys

def fibonacci_partial_sum_naive(from_, to):
    sum = 0

    current = 0
    next  = 1

    for i in range(to + 1):
        if i >= from_:
            sum += current

        current, next = next, current + next

    return sum % 10

def fn(n):
    f0 = 0
    f1 = 1
    if n == 0:
        return f0
    elif n == 1:
        return f1
    else:
        rem = n % 60
        if rem == 0:
            return 0
        for i in range(2, rem + 3):
            f =(f0 + f1)% 60
            f0, f1 = f1, f
        s = f1 - 1
        return s

if __name__ == '__main__':
    fr, to = map(int, input().split())
    # print(fibonacci_partial_sum_naive(from_, to))
    print((fn(to) - fn(fr - 1)) % 10)