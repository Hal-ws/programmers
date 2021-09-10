from collections import deque


def solution(game_board, table):
    answer = -1
    n, m = len(game_board), len(table)
    cnt = 2  # 2번 빈 공간부터 시작
    for i in range(n):
        for j in range(n):
            if game_board[i][j] == 0: # 빈공간 발견. 색칠 후 채워넣을 수 있는 puzzle 찾음
                area = coloring(game_board, cnt, i, j, n)
                cnt += 1

    return answer


def coloring(game_board, color, y, x, n):  # game_board의 빈 공간을 원하는 cnt로 색칠함
    dy, dx = [-1, 1, 0, 0], [0, 0, -1, 1]
    visit = [[0 for j in range(n)] for i in range(n)]
    visit[y][x] = 1
    q = deque()
    q.append([y, x])
    area = 1
    game_board[y][x] = color
    while len(q) > 0:
        
    return 0


def findPuzzle(game_board, cnt, table):  # table에서 game_board에 해당하는 cnt와 겹칠 수 있는 puzzle을 찾음
    return 0

