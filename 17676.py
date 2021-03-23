from copy import deepcopy

def solution(lines):
    l = len(lines)
    timeTable, processingTimes = [], []
    for i in range(l):
        day, end, time = map(str, lines[i].split())
        timeTable.append([int(end[:2]), int(end[3:5]), int(end[6:8]), float('0' + end[8:12])])
        timeTable[i] = getsecondscale(timeTable[i], float(time[:len(time) - 1]))
    timeTable = sorted(timeTable)
    for i in range(l):
        print(timeTable[i])
    answer = 0
    for i in range(l):
        firstProcessEnd = i
        untilEndFlag = 1
        for j in range(i + 1, l):
            if round(timeTable[j][1] - timeTable[firstProcessEnd][0], 3) >= 1: ##
                lastProcessStart = j - 1
                untilEndFlag = 0
                break
        if untilEndFlag:
            temp = l - firstProcessEnd
        else:
            temp = lastProcessStart - firstProcessEnd + 1
        if answer <= temp:
            answer = temp
    print(answer)
    return answer


def getsecondscale(endTime, processingTime):
    processingTime = [processingTime // 1, round(processingTime % 1, 3)]
    temp = deepcopy(endTime)
    startTime = round(temp[0] * pow(60, 2) + temp[1] * pow(60, 1) + temp[2] + temp[3] - processingTime[0] - processingTime[1] + 0.001, 3)
    endTime = endTime[0] * pow(60, 2) + endTime[1] * pow(60, 1) + endTime[2] + endTime[3]
    return [endTime, startTime]



solution(["2016-09-15 01:00:04.002 2.0s", "2016-09-15 01:00:07.000 2s"])
