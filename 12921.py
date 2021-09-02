from math import sqrt


def solution(n):
    answer = 0
    eratos = [1] * (1000001)
    eratos[0], eratos[1] = 0, 0
    maxNum = int(sqrt(1000000)) + 1
    primeList = []
    for i in range(2, maxNum):
        if eratos[i]: # 소수일때
            for j in range(i + i, 1000001, i):
                eratos[j] = 0
    for i in range(2, n + 1):
        answer += eratos[i]
    return answer
