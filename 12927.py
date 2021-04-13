def solution(n, works):
    answer = 0
    left, right = 0, max(works)
    while left <= right:
        mid = (left + right) // 2 # 최대로 남은 작업량이 mid만큼 되도록 한다
        usedT = 0
        for amount in works:
            if mid <= amount:
                usedT += (amount - mid)
        if usedT <= n: # 가능함
            maxAmout = mid
            right = mid - 1 # 좀 더 일하게 한다
        else:
            left = mid + 1 # 좀 덜 일하게 한다
    usedT = 0
    for i in range(len(works)):
        if works[i] >= maxAmout:
            usedT += (works[i] - maxAmout)
            works[i] = maxAmout
    works.sort(reverse=True)
    leftT = n - usedT
    for i in range(len(works)):
        if leftT > 0:
            if works[i] > 0:
                works[i] -= 1
                leftT -= 1
        else:
            break
    for i in range(len(works)):
        answer += pow(works[i], 2)
    return answer
