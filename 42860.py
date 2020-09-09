def solution(name):
    distance, answer, ln = [], 0, len(name)
    leftflag = 0 # 한번이라도 왼쪽으로 움직이면 계속 왼쪽으로만 감
    for i in range(ln):
        distance.append(ord(name[i]) - 65)
        if distance[i] > 13:
            distance[i] = 26 - distance[i]
    maxcnt = ln - distance.count(0)
    i, idx = 0, 0
    while i < maxcnt:
        answer += distance[idx]
        if leftflag:
            nextIdx = nextleft(distance, idx)
            answer += (idx + ln - nextIdx)
            idx = nextIdx
        else: 

        i += 1





    print(distance)
    return answer

def nextright(distance, idx):
    l = len(distance)
    for i in range(idx + 1, l):
        if distance[i] != 0:
            return i - idx ## 다음 문자까지의 거리
    return -1 ## 끝까지 다봄

def nextleft(distance, idx):
    return idx
solution("JEROEN")
