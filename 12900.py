def solution(n):
    dp = [1, 2]
    for i in range(n - 2):
        tmp = (dp[0] + dp[1]) % 1000000007
        dp[0] = dp[1]
        dp[1] = tmp
    answer = dp[1]
    return answer
