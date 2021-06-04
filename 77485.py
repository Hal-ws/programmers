from _collections import deque


def solution(rows, columns, queries):
    answer = []
    board = [[i * columns + j + 1 for j in range(columns)] for i in range(rows)]
    for query in queries:
        answer.append(rotating(query, board))
    return answer


def rotating(query, board):
    y1, x1, y2, x2 = query[0] - 1, query[1] - 1, query[2] - 1, query[3] - 1
    minVal = 10001
    q = deque()
    for j in range(x1, x2 + 1):
        q.append(board[y1][j])
        if q[-1] < minVal:
            minVal = q[-1]
    for i in range(y1 + 1, y2 + 1):
        q.append(board[i][x2])
        if q[-1] < minVal:
            minVal = q[-1]
    for j in range(x2 - 1, x1 - 1, -1):
        q.append(board[y2][j])
        if q[-1] < minVal:
            minVal = q[-1]
    for i in range(y2 - 1, y1, -1):
        q.append(board[i][x1])
        if q[-1] < minVal:
            minVal = q[-1]
    q.appendleft(q.pop())
    for j in range(x1, x2 + 1):
        board[y1][j] = q.popleft()
    for i in range(y1 + 1, y2 + 1):
        board[i][x2] = q.popleft()
    for j in range(x2 - 1, x1 - 1, -1):
        board[y2][j] = q.popleft()
    for i in range(y2 - 1, y1, -1):
        board[i][x1] = q.popleft()
    return minVal
