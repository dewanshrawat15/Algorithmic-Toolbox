# Uses python3

def get_change_rec_dp(m, dp):
    #write your code here
    if m == 0:
        return 1
    ways = []
    if m - 4 >= 0:
        if dp[m - 4] == -1:
            dp[m - 4] = get_change_rec_dp(m - 4, dp)
        ways.append(dp[m - 4])
    if m - 3 >= 0:
        if dp[m - 3] == -1:
            dp[m - 3] = get_change_rec_dp(m - 3, dp)
        ways.append(dp[m - 3])
    if m - 1 >= 0:
        if dp[m - 1] == -1:
            dp[m - 1] = get_change_rec_dp(m - 1, dp)
        ways.append(dp[m - 1])
    return min(ways) + 1

def get_change_it(m):
    if m == 0:
        return 0
    if m == 1:
        return 1
    if m == 2:
        return 2
    dp = [0] + [10**9] * m
    dp[1] = 1
    dp[2] = 2
    denominations = [1, 3, 4]
    for i in range(3, m + 1):
        for j in denominations:
            if i >= j:
                coins = dp[i - j] + 1
                if coins < dp[i]:
                    dp[i] = coins
    return dp[-1]


if __name__ == '__main__':
    m = int(input())
    dp = [-1 for i in range(m)]
    print(get_change_it(m))