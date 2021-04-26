import heapq
from math import inf


def solution(N, road, K):
    answer = 0
    disHeap = []
    dis = [inf for i in range(N + 1)]
    connect = [[] for i in range(N + 1)]
    for tmp in road:
        a, b, t = tmp[0], tmp[1], tmp[2]
        connect[a].append([t, b])
        connect[b].append([t, a])
    heapq.heappush(disHeap, [0, 1])
    dis[1] = 0
    while len(disHeap) > 0:
        tmp = heapq.heappop(disHeap)
        curP, curT = tmp[1], tmp[0]
        for nxt in connect[curP]:
            totalT, nxtP = curT + nxt[0], nxt[1]
            if totalT < dis[nxtP]:
                heapq.heappush(disHeap, [totalT, nxtP])
                dis[nxtP] = totalT
    for i in range(1, N + 1):
        if dis[i] <= K:
            answer += 1
    return answer
