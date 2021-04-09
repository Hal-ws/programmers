def solution(a):
    global answer, nList
    answer = 0
    cntList = [[0, i] for i in range(len(a))] #수 i가 0개 있음
    for num in a:
        cntList[num][0] += 1
    nList = a
    cntList.sort(reverse=True)
    for tmp in cntList:
        maxLen = 2 * tmp[0]
        std = tmp[1]
        if maxLen <= answer:
            break
        if maxLen != 0:
            getstarlen(std, nList, maxLen)
    return answer


def getstarlen(std, nList, maxLen):
    global answer
    flag1, flag2 = 0, 0
    starLen = 0
    for num in nList:
        if num != std:
            flag1 = 1
        else:
            flag2 = 1
        if flag1 == 1 and flag2 == 1:
            starLen += 2
            flag1, flag2 = 0, 0
        if maxLen == starLen:
            break
    if starLen > answer:
        answer = starLen
