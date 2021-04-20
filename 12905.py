def solution(board):
    answer = 0
    w, h = len(board[0]), len(board)
    dp = [[0 for j in range(w)] for i in range(h)]
    for j in range(w):
        if board[0][j]:
            dp[0][j] = 1
    for i in range(h):
        if board[i][0]:
            dp[i][0] = 1
    for i in range(1, h):
        for j in range(1, w):
            if board[i][j]:
                dp[i][j] = 1
                if board[i - 1][j] * board[i][j - 1] > 0:
                    minL = min(dp[i - 1][j], dp[i][j - 1])
                    if board[i - minL][j - minL] == 1:
                        dp[i][j] = minL + 1
                    else:
                        dp[i][j] = minL
    for i in range(h):
        for j in range(w):
            if dp[i][j] * dp[i][j] > answer:
                answer = dp[i][j] * dp[i][j]
    return answer
