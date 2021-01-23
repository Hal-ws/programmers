def solution(tickets):
    global possible, maxCnt
    maxCnt = len(tickets) # 총 티켓의 수
    possible = []
    for i in range(maxCnt):
        if tickets[i][0] == "ICN": #인천에서 출발하는 비행기
            used = [0] * maxCnt
            used[i] = 1 # i번 티켓을 사용함
            dfs(tickets[i][1], used, tickets, 1, [i])
    possible.sort()
    return possible[0]


def dfs(port, used, tickets, cnt, path): # 도착한 공항, used, tickets정보, 사용 티켓 수, 사용 티켓정보(순서)
    global possible, maxCnt
    if cnt == maxCnt:
        tmp = ['ICN']
        for i in range(maxCnt):
            tmp.append(tickets[path[i]][1])
        possible.append(tmp)
        return
    for i in range(maxCnt):
        if used[i] == 0: #아직 사용 안한 티켓일때
            if port == tickets[i][0]: #현재 port 에서 출발할수 있는 티켓일 때
                used[i] = 1
                path.append(i)
                dfs(tickets[i][1], used, tickets, cnt + 1, path)
                used[i] = 0
                path.pop()
