from collections import deque


def solution(game_board, table):
    # 테이블을 돌아가면서 puzzle 획득 -> 해당 퍼즐을 끼워맞출수 있는 곳 찾음 -> 퍼즐 삭제
    global dy, dx
    dy, dx = [-1, 1, 0, 0], [0, 0, -1, 1]
    answer = 0
    n, m = len(game_board), len(table)
    holeAreas = [None, None] ## 각각 idx를 매기면서, hole의 area를 기록함
    cnt = 2
    for i in range(n):
        for j in range(n):
            if game_board[i][j] == 0:
                holeAreas.append(getArea(game_board, i, j, n, cnt))
                cnt += 1
    for i in range(m):
        for j in range(m):
            if table[i][j] == 1: # 아직 안쓴 puzzle 발견
                puzzle = getpuzzle(table, i, j, m)
                result = findhole(game_board, puzzle, holeAreas, n) # hole을 채울수 있는지 아닌지 확인
                if result > 0:
                    answer += result
                erasing(table, i, j, m) # 해당 puzzle 삭제
    return answer


def findhole(game_board, puzzle, holeArea, n):
    area = 0
    for i in range(len(puzzle)):
        for j in range(len(puzzle[0])):
            area += puzzle[i][j]
    for _ in range(4):  # 회전하면서 game_board에 딱 맞게 들어가는걸 찾음
        puzzle = rotating(puzzle)
        result = matching(game_board, puzzle, holeArea, n, area)
        if result > 0:  # 매칭가능하면 puzzle의 넓이 return
            return result
    return 0


def matching(game_board, puzzle, holeArea, n, area):
    w, h = len(puzzle[0]), len(puzzle) # puzzle의 가로, 세로
    for sy in range(n - h + 1):
        for sx in range(n - w + 1):
            flag = 1
            for py in range(h):
                for px in range(w):
                    if puzzle[py][px] == 0 and game_board[sy + py][sx + px] != 1:
                        flag = 0
                        break
                    if puzzle[py][px] == 1 and game_board[sy + py][sx + px] == 1:
                        flag = 0
                        break
            if flag:
                idx = 0
                pFlag = 1
                for py in range(h):
                    for px in range(w):
                        if game_board[sy + py][sx + px] > 1 and holeArea[game_board[sy + py][sx + px]] != None:
                            if idx == 0:
                                idx = game_board[sy + py][sx + px]
                            elif game_board[sy + py][sx + px] != idx:
                                pFlag = 0
                                break
                if pFlag:
                    if holeArea[idx] == area:
                        holeArea[idx] = None  # 해당 hole은 꽉 참
                        return area
    return 0


def getArea(game_board, y, x, n, cnt):
    visit = [[0 for j in range(n)] for i in range(n)]
    visit[y][x] = 1
    q = deque()
    q.append([y, x])
    area = 1
    while len(q) > 0:
        tmp = q.popleft()
        y, x = tmp[0], tmp[1]
        game_board[y][x] = cnt
        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]
            if 0 <= ny < n and 0 <= nx < n and visit[ny][nx] == 0 and game_board[ny][nx] == 0:
                visit[ny][nx] = 1
                area += 1
                q.append([ny, nx])
    return area


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


def rotating(puzzle):
    w, h = len(puzzle[0]), len(puzzle)
    newPuzzle = [[0 for j in range(h)] for i in range(w)]
    for i in range(h):
        for j in range(w):
            newPuzzle[j][h - 1 - i] = puzzle[i][j]
    return newPuzzle
