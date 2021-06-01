from itertools import combinations


def solution(n):
    answer = pow(10, 7)
    biN = str(bin(n))
    biN = biN[2:]
    cnt, l = biN.count('1'), len(biN)
    list1 = [i for i in range(l)]
    cases = list(combinations(list1, cnt))
    for case in cases:
        i = 0
        tmp = 0
        for j in range(l):
            if case[i] == j:
                tmp += pow(2, case[i])
                i += 1
            if i == cnt:
                break
        if tmp > n and tmp < answer:
            answer = tmp
    list2 = [i for i in range(l + 1)]
    cases = list(combinations(list2, cnt))
    for case in cases:
        i = 0
        tmp = 0
        for j in range(l + 1):
            if case[i] == j:
                tmp += pow(2, case[i])
                i += 1
            if i == cnt:
                break
        if tmp > n and tmp < answer:
            answer = tmp
    return answer
