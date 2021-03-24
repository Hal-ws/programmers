def solution(n, times):
    maxT = max(times)
    left, right = 0, maxT * n + 1
    answer = right
    while left <= right:
        mid = (left + right) // 2
        if chkvalid(n, times, mid): # 가능함
            answer = mid
            right = mid - 1
        else: # 불가능함. 시간 더 키워야함
            left = mid + 1
    return answer


def chkvalid(n, times, val):
    result = 0
    for i in range(len(times)):
        maxP = val // times[i] # i번 심사관이 최대로 검사 가능한 사람 수
        result += maxP
        if n <= result:
            return 1
    return 0
