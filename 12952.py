def solution(n):
    global board, answer
    answer = 0
    board = [[0 for j in range(n)] for i in range(n)]
    for j in range(n):
        dfs(0, j, n)
    return answer


def dfs(i, j, n): # 지금 놓은 좌표
    global board, answer
    if i == n - 1 and chk(i, j, n):
        answer += 1
        return
    board[i][j] = 1
    if chk(i, j, n): # 배치 가능 확인
        for k in range(n):
            if k != j - 1 and k != j and k != j + 1:
                dfs(i + 1, k, n)
    else:
        board[i][j] = 0
        return 0
    board[i][j] = 0


def chk(i, j, n): # i, j 배치가 가능한지 확인
    for y in range(i - 1, -1, -1): # 위로
        if board[y][j] == 1:
            return 0
    for d in range(1, n):
        y, x = i - d, j - d
        if y == -1 or x == -1:
            break
        if board[y][x] == 1:
            return 0
    for d in range(1, n):
        y, x = i - d, j + d
        if y == -1 or x == n:
            break
        if board[y][x] == 1:
            return 0
    return 1
