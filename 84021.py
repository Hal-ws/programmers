from collections import deque


def solution(game_board, table):
    # 테이블을 돌아가면서 puzzle 획득 -> 해당 퍼즐을 끼워맞출수 있는 곳 찾음 -> 퍼즐 삭제
    global dy, dx
    dy, dx = [-1, 1, 0, 0], [0, 0, -1, 1]
    answer = 0
    n, m = len(game_board), len(table)
    for i in range(m):
        for j in range(m):
            if table[i][j] == 1: # 아직 안쓴 puzzle 발견
                puzzle = getpuzzle(table, i, j, m)
                for k in range(len(puzzle)):
                    print(puzzle[k])
                return
                erasing(table, i, j, m) #
                result = findhole(game_board, puzzle, n) # hole을 채울수 있는지 아닌지 확인
                if result > 0:
                    answer += result
    return answer


def getpuzzle(table, y, x, m):
    uBound, lBound, dBound, rBound = 50, 50, -1, -1
    q = deque()
    visit = [[0 for j in range(m)] for i in range(m)]
    visit[y][x] = 1
    q.append([y, x])
    while len(q) > 0:
        tmp = q.popleft()
        y, x = tmp[0], tmp[1]
        if y < uBound:
            uBound = y
        if y > dBound:
            dBound = y
        if x < lBound:
            lBound = x
        if x > rBound:
            rBound = x
        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]
            if 0 <= ny < m and 0 <= nx < m and visit[ny][nx] == 0 and table[ny][nx] == 1:
                visit[ny][nx] = 1
                q.append([ny, nx])
    puzzle = [[0 for j in range(rBound - lBound + 1)] for i in range(dBound - uBound + 1)]
    for i in range(uBound, dBound + 1):
        for j in range(lBound, rBound + 1):
            puzzle[i - uBound][j - lBound] = table[i][j]
    return puzzle


def erasing(table, y, x, m):  #table에서 사용한 puzzle 삭제
    visit = [[0 for j in range(m)] for i in range(m)]
    visit[y][x] = 1
    table[y][x] = 0
    q = deque()
    q.append([y, x])
    while len(q) > 0:
        tmp = q.popleft()
        y, x = tmp[0], tmp[1]
        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]
            if 0 <= ny < m and 0 <= nx < m and visit[ny][nx] == 0 and table[ny][nx] == 1:
                table[ny][nx] = 0
                visit[ny][nx] = 1
                q.append([ny, nx])


def findhole(game_board, puzzle, n):
    w, h = len(puzzle[0]), len(puzzle)
    

    return 1


solution([[1,1,0,0,1,0],[0,0,1,0,1,0],[0,1,1,0,0,1],[1,1,0,1,1,1],[1,0,0,0,1,0],[0,1,1,1,0,0]],
         [[0,0,0,1,1,0],
          [0,0,1,0,1,0],
          [0,1,1,0,1,1],
          [0,0,1,0,0,0],
          [1,1,0,1,1,0],
          [0,1,0,0,0,0]])
