def solution(n, costs):
    lc = len(costs)
    for i in range(lc):
        if costs[i][0] < costs[i][1]:
            costs[i][0], costs[i][1], costs[i][2] = costs[i][2], costs[i][0], costs[i][1]
        else:
            costs[i][0], costs[i][1], costs[i][2] = costs[i][2], costs[i][1], costs[i][0]
    cycle = []
    for i in range(n):
        cycle.append([i, i])
    costs.sort()
    answer = 0
    return answer


def getparent(idx, cycle):
    if cycle[idx][1] == cycle[idx][0]:
        return idx
    return getparent(cycle[idx][1], cycle)

def unionparent(idx1, idx2, cycle):
    a = getparent(idx1, cycle)
    b = getparent(idx2, cycle)
    if a == b: # 둘 다 root node가 같음
        return;



solution(5, [[0,1,1],[0,2,2],[1,2,5],[1,3,1],[2,3,8]])
