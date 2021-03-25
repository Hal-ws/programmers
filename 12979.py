def solution(n, stations, w):
    seperated = []
    first = stations[0]
    answer = 0
    if first - w - 1 > 0:
        seperated.append(first - w - 1)
    for i in range(1, len(stations)):
        dis = stations[i] - stations[i - 1] # 중계국 사이의 거리
        if dis - 2 * w - 1 > 0:
            seperated.append(dis - 2 * w - 1)
    last = n - stations[-1] - w
    if last > 0:
        seperated.append(last)
    for d in seperated:
        answer += set5g(d, w)
    return answer


def set5g(d, w):
    coverR = w * 2 + 1
    cnt = d // coverR
    if d % coverR != 0:
        cnt += 1
    return cnt
