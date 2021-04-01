def solution(a):
    N = len(a)
    rightD = [None for i in range(N)]
    leftD = [None for i in range(N)]
    rightD[0] = a[0]
    leftD[N - 1] = a[N - 1]
    answer = 0
    for i in range(1, N):
        val = a[i]
        if val < rightD[i - 1]:
            rightD[i] = val
        else:
            rightD[i] = rightD[i - 1]
    for i in range(N - 2, -1, -1):
        val = a[i]
        if val < leftD[i + 1]:
            leftD[i] = val
        else:
            leftD[i] = leftD[i + 1]
    for i in range(N):
        val = a[i]
        if i == 0 or i == N - 1:
            answer += 1
            continue
        leftMin, rightMin = rightD[i - 1], leftD[i + 1]
        if val < leftMin and val < rightMin:
            answer += 1
        else:
            if (leftMin - val) * (rightMin - val) < 0:
                answer += 1
    return answer
