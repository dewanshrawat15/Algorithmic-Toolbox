# Uses python3
from sys import setrecursionlimit
setrecursionlimit(10 ** 4)

def get_change(m, dp):
    if m == 0:
        return 1
    ways = []
    if m - 10 >= 0:
        if dp[m - 10] == -1:
            dp[m - 10] = get_change(m - 10, dp)
        ways.append(dp[m - 10])
    if m - 5 >= 0:
        if dp[m - 5] == -1:
            dp[m - 5] = get_change(m - 5, dp)
        ways.append(dp[m - 5])
    if m - 1 >= 0:
        if dp[m - 1] == -1:
            dp[m - 1] = get_change(m - 1, dp)
        ways.append(dp[m - 1])
    return min(ways) + 1

# 32
# 31 + 1, 27 + 5, 22 + 10

if __name__ == '__main__':
    m = int(input())
    dp = [-1 for i in range(m)]
    print(get_change(m, dp) - 1)
