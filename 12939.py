def solution(s):
    numList = sorted(list(map(int, s.split())))
    answer = str(numList[0]) + ' ' + str(numList[-1])
    return answer
