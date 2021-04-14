def solution(distance, rocks, n):
    left, right = 0, distance
    rocks = sorted([0] + rocks + [distance])
    answer = 0
    l = len(rocks)
    print('rocks: %s' %rocks)
    while left <= right:
        cnt = 0
        accDis = 0
        minDis = distance + 1
        mid = (left + right) // 2 # 거리의 최솟값이 mid 를 만족하는지 확인
        print('mid: %s' %mid)
        for i in range(1, l):
            dis = accDis + rocks[i] - rocks[i - 1]
            print('dis: %s' %dis)
            if dis < mid: #dis가 mid보다 작음. 바위 삭제 필요
                if i == l - 1:
                    cnt = n + 1
                    break
                print('%sth rock break' %i)
                accDis += (rocks[i] - rocks[i - 1])
                cnt += 1
            else: # 바위 삭제할 필요 없음
                accDis = 0
                if dis < minDis:
                    minDis = dis
            if i == l - 1: # 도착지
                if dis < minDis:
                    minDis = dis
        print('cnt, minDis: %s, %s' %(cnt, minDis))
        if cnt > n: # 허용치 이상으로 부숨. mid를 줄여야
            right = mid - 1
        elif cnt < n: # 적게 부숨.
            left = mid + 1
        else:
            if answer < mid:
                answer = mid
            left = mid + 1
        print('-----------------------')
    return answer


print(solution(10, [3, 5, 6, 9], 1))
