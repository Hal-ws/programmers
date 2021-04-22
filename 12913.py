def solution(land):
    dp = [[0 for j in range(len(land[0]))] for i in range(len(land))]
    for j in range(4):
        dp[0][j] = land[0][j]
    for i in range(1, len(land)):
        for j in range(4):
            if j == 0:
                dp[i][j] = max(dp[i - 1][1], dp[i - 1][2], dp[i - 1][3])
            if j == 1:
                dp[i][j] = max(dp[i - 1][0], dp[i - 1][2], dp[i - 1][3])
            if j == 2:
                dp[i][j] = max(dp[i - 1][0], dp[i - 1][1], dp[i - 1][3])
            if j == 3:
                dp[i][j] = max(dp[i - 1][0], dp[i - 1][1], dp[i - 1][2])
            dp[i][j] += land[i][j]
    return max(dp[-1])
