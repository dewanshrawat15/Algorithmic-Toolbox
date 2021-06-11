# Uses python3
import sys

def fibonacci_sum_naive(n):
    if n <= 1:
        return n

    previous = 0
    current  = 1
    sum      = 1

    for _ in range(n - 1):
        previous, current = current, previous + current
        sum += current

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
    n = int(input())
    # print(fibonacci_sum_naive(n))
    print(fn(n) % 10)