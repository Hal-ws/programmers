def solution(n):
    dp = [0, 1]
    if n < 2:
        return dp[n - 1]
    for i in range(n - 1):
        tmp = (dp[0] + dp[1]) % 1234567
        dp[0] = dp[1]
        dp[1] = tmp
    return dp[1]
