def solution(n):
    n = list(str(n))
    n.sort(reverse=1)
    answer = ''
    for num in n:
        answer += num
    return int(answer)
