from _collections import deque


def solution(n, results):
    global win, lose
    win = [[] for i in range(n + 1)] # i번 선수가 이긴 사람들 저장
    lose = [[] for i in range(n + 1)] # i번 선수를 이긴사람 저장
    answer = 0
    for match in results:
        a, b = match[0], match[1]
        win[a].append(b)
        lose[b].append(a)
    for i in range(1, n + 1):
        winCnt = getwincnt(i, n)
        loseCnt = getlosecnt(i, n)
        if winCnt + loseCnt == n - 1:
            answer += 1
    return answer


def getwincnt(p, n):
    global win
    visit = [0 for i in range(n + 1)]
    q = deque()
    q.append(p)
    visit[p] = 1
    cnt = 0
    while len(q) > 0:
        cur = q.popleft()
        for nxt in win[cur]:
            if visit[nxt] == 0:
                visit[nxt] = 1
                q.append(nxt)
                cnt += 1
    return cnt


def getlosecnt(p, n):
    global lose
    visit = [0 for i in range(n + 1)]
    q = deque()
    q.append(p)
    visit[p] = 1
    cnt = 0
    while len(q) > 0:
        cur = q.popleft()
        for nxt in lose[cur]:
            if visit[nxt] == 0:
                visit[nxt] = 1
                q.append(nxt)
                cnt += 1
    return cnt
