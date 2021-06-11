# Uses python3

def fibonacci_sum_squares_naive(n):
    if n <= 1:
        return n

    previous = 0
    current  = 1
    sum      = 1

    for _ in range(n - 1):
        previous, current = current, previous + current
        sum += current * current

    return sum % 10

def period(m):
    a, b = 0, 1
    c = a + b
    for i in range(pow(m, 2)):
        c = (a + b) % m
        a, b = b, c
        if a == 0 and b == 1:
            return i + 1

def fn(n, m):
    remainder = n % period(m)
    first = 0
    second = 1
    res = remainder
    for i in range(1, remainder):
        res = (first + second) % m
        first, second = second, res
    return res % m

if __name__ == '__main__':
    n = int(input())
    # print(fibonacci_sum_squares_naive(n))
    print((fn(n + 1, 10) * fn(n, 10)) % 10)