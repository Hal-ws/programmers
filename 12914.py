def solution(n):
    dp = [[0, 0] for i in range(n + 1)]
    dp[1][0] = 1
    for i in range(2, n + 1):
        if i == 2:
            dp[i][0] = 1
            dp[i][1] = 1
        else:
            dp[i][0] = (dp[i - 1][0] + dp[i - 1][1]) % 1234567
            dp[i][1] = (dp[i - 2][0] + dp[i - 2][1]) % 1234567
    answer = sum(dp[n]) % 1234567
    return answer
