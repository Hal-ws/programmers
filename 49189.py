from collections import deque

def solution(n, edge):
    connect = [[] for i in range(n + 1)]
    for i in range(len(edge)):
        a, b = edge[i][0], edge[i][1]
        connect[a].append(b)
        connect[b].append(a)
    visit = [0] * (n + 1)
    q = deque()
    q.append([1, 0]) #node, 거리
    visit[1] = 1
    cnt = 0
    maxDis = 0
    while len(q) > 0:
        cur = q[0][0]
        dis = q[0][1]
        for next in connect[cur]:
            if visit[next] == 0:
                visit[next] = 1
                q.append([next, dis + 1])
                if maxDis < dis + 1:
                    maxDis = dis + 1
                    cnt = 1
                elif maxDis == dis + 1:
                    cnt += 1
        q.popleft()
    return cnt
