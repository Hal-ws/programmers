from collections import deque


def solution(numbers, target):
    q = deque()
    q.append([0, 0]) # 연산한 수의 갯수, 수의 합
    answer = 0
    for cnt in range(1, len(numbers) + 1): # cnt번째 수를 더하거나 뺌
        num = numbers[cnt - 1]
        while 1:
            if q[0][0] == cnt: # 이번 수행에서 한 결과임
                break
            tmp = q.popleft()
            q.append([tmp[0] + 1, tmp[1] + num])
            q.append([tmp[0] + 1, tmp[1] - num])
    while len(q) > 0:
        tmp = q.popleft()
        if tmp[1] == target:
            answer += 1
    return answer
