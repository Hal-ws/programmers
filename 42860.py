def solution(name):
    diff, answer, ln = [], 0, len(name)
    jumpflag = 0 # 왼쪽 끝에서 점프했는지 확인
    for i in range(ln):
        diff.append(ord(name[i]) - 65)
        if diff[i] > 13:
            diff[i] = 26 - diff[i]
    maxcnt = ln - diff.count(0)
    i, idx = 0, 0
    while i < maxcnt:
        answer += diff[idx]
        diff[idx] = 0
        lDistance, rDistance = nextleft(diff, idx), nextright(diff, idx)
        if rDistance == None:
            break
        if rDistance <= lDistance:
            answer += rDistance
            idx += rDistance
        else:
            jumpflag = 1 # 점프해준 후 다음 idx 지정, 다음 idx 까지 거리는 answer에 더해줌
            answer += lDistance
            idx = ln + idx - lDistance
            break
        i += 1
    if jumpflag:
        std = idx
        while idx >= 0:
            if diff[idx] > 0:
                answer += std - idx
                answer += diff[idx]
                diff[idx] = 0
                std = idx
            idx -= 1
    return answer


def nextright(diff, idx):
    l = len(diff)
    for i in range(idx + 1, l):
        if diff[i] != 0:
            return i - idx ## 다음 문자까지의 거리

def nextleft(diff, idx):
    l = len(diff)
    for i in range(l - 1, -1, -1):
        if diff[i] != 0:
            return idx + l - i
