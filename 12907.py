def solution(n, money):
    money.sort()
    l = len(money)
    dp = [[0 for j in range(n + 1)] for i in range(l + 1)]
    for j in range(1, n + 1):
        for i in range(l):
            coin = money[i]
            idx = i + 1
            dp[idx][j] += dp[idx - 1][j]
            if coin <= j:
                if coin == j:
                    dp[idx][j] += 1
                else:
                    dp[idx][j] += dp[idx][j - coin]
            dp[idx][j] = dp[idx][j] % 1000000007
    return dp[l][n] % 1000000007
