def solution(routes):
    answer = 1
    routes.sort()
    coverT = routes[0][1] # 현재 범위가 커버하는 시간
    for i in range(1, len(routes)):
        start, end = routes[i][0], routes[i][1]
        if start <= coverT: # 현재 범위가 포함됨
            if end < coverT:
                coverT = end
        else: # 새 cctv 설치 필요
            coverT = end
            answer += 1
    return answer
