def solution(strings, n):
    answer = [[None, None] for i in range(len(strings))]
    for i in range(len(strings)):
        answer[i][0] = strings[i][n]
        answer[i][1] = strings[i]
    answer.sort()
    for i in range(len(answer)):
        answer[i] = answer[i][1]
    return answer
