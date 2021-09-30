def solution(numbers):
    answer = 0
    visit = [1] * 10
    for nIdx in numbers:
        visit[nIdx] = 0
    for i in range(10):
        if visit[i]:
            answer += i
    return answer
