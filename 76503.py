from _collections import deque


def solution(a, edges):
    cnt = 0
    linkCnt = [0 for i in range(len(a))]
    connect = [[] for i in range(len(a))]
    visit = [0 for i in range(len(a))]
    for i in range(len(edges)):
        s, e = edges[i][0], edges[i][1]
        connect[s].append(e)
        connect[e].append(s)
        linkCnt[s] += 1
        linkCnt[e] += 1
    q = deque()
    for node in range(len(a)):
        if linkCnt[node] == 1:
            q.append(node)
    while len(q) > 0:
        curNode = q.popleft() # 현재 node. node에 있는 가중치를 0으로 만든다
        weight = a[curNode]
        visit[curNode] = 1
        for nxtNode in connect[curNode]:
            if visit[nxtNode] == 0:
                a[nxtNode] += weight
                a[curNode] = 0
                cnt += abs(weight)
                linkCnt[nxtNode] -= 1
                if linkCnt[nxtNode] == 1:
                    q.append(nxtNode)
    for amount in a:
        if amount != 0:
            return -1
    return cnt
