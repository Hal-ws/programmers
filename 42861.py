def solution(n, costs):
    global roots
    answer = 0
    roots = [i for i in range(n)]
    for i in range(len(costs)):
        costs[i][0], costs[i][2] = costs[i][2], costs[i][0]
    costs.sort()
    for path in costs:
        dis, node1, node2 = path[0], path[1], path[2]
        root1, root2 = find(node1), find(node2)
        if root1 != root2:
            union(root1, root2)
            answer += dis
    return answer


def union(node1, node2):
    global roots
    root1, root2 = find(node1), find(node2)
    if root1 != root2:
        roots[root2] = root1


def find(node):
    global roots
    if roots[node] == node:
        return node
    roots[node] = find(roots[node])
    return roots[node]
