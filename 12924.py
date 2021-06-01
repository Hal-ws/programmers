def solution(n):
    sumList = [0] * (n + 1)
    for i in range(1, n + 1):
        sumList[i] = i + sumList[i - 1]
    answer = 0
    for i in range(1, n + 1):
        answer += chkPossible(i, sumList, n)
    return answer


def chkPossible(getL, sumList, n):
    left, right = 0, n - getL
    while left <= right:
        mid = (left + right) // 2
        if sumList[mid + getL] - sumList[mid] == n:
            return 1
        if sumList[mid + getL] - sumList[mid] < n:
            left = mid + 1
        else:
            right = mid - 1
    return 0
