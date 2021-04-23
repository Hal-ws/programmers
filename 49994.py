def solution(dirs):
    pos = [5, 5]
    answer = 0
    roads = [[0 for j in range(21)] for i in range(21)]
    for d in dirs:
        y, x = pos[0], pos[1]
        ry, rx = y * 2, x * 2
        if d == 'L' and x > 0:
            roads[ry][rx - 1] = 1
            x -= 1
        if d == 'R' and x < 10:
            roads[ry][rx + 1] = 1
            x += 1
        if d == 'U' and y > 0:
            roads[ry - 1][rx] = 1
            y -= 1
        if d == 'D' and y < 10:
            roads[ry + 1][rx] = 1
            y += 1
        pos[0], pos[1] = y, x
    for i in range(len(roads)):
        for j in range(len(roads[0])):
            answer += roads[i][j]
    return answer
