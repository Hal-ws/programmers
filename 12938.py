def solution(n, s):
    if s < n:
        return [-1]
    average = s // n
    answer = [average for i in range(n)]
    s -= (average * n)
    for i in range(s):
        answer[i] += 1
    answer.sort()
    return answer
