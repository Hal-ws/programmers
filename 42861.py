def solution(n, costs):
    lc = len(costs)
    for i in range(lc):
        costs[i][0], costs[i][1], costs[i][2] = costs[i][2], costs[i][0], costs[i][1]
    cycle = []
    for i in range(n):
        cycle.append([i, i])
    costs.sort()
    print(cycle)
    print(costs)

    answer = 0
    return answer

def getparent(idx, cycle):
    if cycle[idx][1] == cycle[idx][0]:
        return idx
    return getparent(cycle[idx][1], cycle)
