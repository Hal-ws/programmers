def solution(s):
    answer = []
    s = s[2:len(s) - 2]
    sList = list(map(str, s.split('},{')))
    cntList = [[0, i] for i in range(100001)]
    for i in range(len(sList)):
        sList[i] = list(map(int, sList[i].split(',')))
    for tu in sList:
        for num in tu:
            cntList[num][0] += 1
    cntList.sort(reverse=True)
    for i in range(100001):
        if cntList[i][0] == 0:
            break
        answer.append(cntList[i][1])
    return answer
