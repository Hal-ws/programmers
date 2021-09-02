def solution(distance, rocks, n):
    left, right = 0, distance
    answer = 0
    rocks.sort()
    rocks = [0] + rocks
    rocks.append(distance)
    while left <= right:
        mid = (left + right) // 2
        chk = chkPossible(rocks, n, mid)
        if chk == 1: # n개를 지우고 거리의 최소값 mid가 가능함
            answer = mid
            left = mid + 1
        else:
            right = mid - 1
    return answer


def chkPossible(rocks, n, chkDis): # 최소 거리가 정확하게 chkDis가 돼야함
    culDis = 0
    minDis = rocks[-1]
    for i in range(1, len(rocks)):
        dis = rocks[i] - rocks[i - 1] + culDis
        if dis < chkDis: # 최소 거리보다 작음
            if n > 0: # 해당 바위를 삭제하고 누적 거리에 계속 추가한다
                n -= 1
                culDis += (rocks[i] - rocks[i - 1])
            else:
                return 0
        else: # 최소 거리보다 같거나 큼
            culDis = 0
            if dis < minDis:
                minDis = dis
    if n == 0: # n개의 바위 부수기 성공
        if chkDis <= minDis: # 목표 거리와 같거나 더 큼. 거리 늘려볼 필요 O
            return 1
        else: # 목표 거리보다 더 짧아짐
            return 0
    else: #다 못부숨. 더 부숴야하니까 거리 늘려봄
        return 1
