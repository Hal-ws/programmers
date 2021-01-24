## 시간초과한 코드...

def solution(n, results):
    global board, connect
    answer = 0
    board = [[[0] * n,[0] * n] for i in range(n)]
    connect = [[[], []] for i in range(n)]
    for match in results:
        winner, loser = match[0] - 1, match[1] - 1
        connect[winner][1].append(loser)
        connect[loser][0].append(winner)
    for i in range(n):
        if connect[i][0] == []:
            dfs([i], i, n)
    for i in range(n):
        tmp = [0] * n
        for j in range(n):
            tmp[j] += board[i][0][j]
            tmp[j] += board[i][1][j]
        tmp[i] = 1
        if tmp == [1] * n:
            answer += 1
    return answer


def dfs(path, p, n): #path, 지금 player, 총 player 수
    global board, connect
    flag = 0 # p가 이긴 상대가 있음
    for nxt in connect[p][1]:
        flag = 1
        path.append(nxt)
        for i in range(n):
            if board[p][0][i] == 1:
                board[nxt][0][i] = 1
        board[nxt][0][p] = 1
        dfs(path, nxt, n)
        path.pop()
    if flag == 0:
        for i in range(len(path) - 1, 0, -1):
            for j in range(i - 1, -1, -1):
                board[path[j]][1][path[i]] = 1


print(solution(5, [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]))
