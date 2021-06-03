def solution(arr):
    global cnt0, cnt1
    cnt0, cnt1 = 0, 0
    deviding([0, 0], [len(arr) - 1, len(arr) - 1], arr)
    return [cnt0, cnt1]


def deviding(leftUp, rightDown, arr): # 왼쪽 위, 오른쪽 아래의 좌표를 표시
    global cnt0, cnt1
    luy, lux = leftUp[0], leftUp[1]
    rdy, rdx = rightDown[0], rightDown[1]
    std = arr[luy][lux]
    flag = 1
    l = rdy - luy + 1
    for i in range(luy, rdy + 1):
        for j in range(lux, rdx + 1):
            if arr[i][j] != std:
                flag = 0
                break
        if flag == 0:
            break
    if flag: # 압축 가능
        if std == 0:
            cnt0 += 1
        else:
            cnt1 += 1
    else:
        deviding([luy, lux], [luy + l // 2 - 1, lux + l // 2 - 1], arr)
        deviding([luy, lux + l // 2], [luy + l // 2 - 1, rdx], arr)
        deviding([luy + l // 2, lux], [rdy, lux + l // 2 - 1], arr)
        deviding([luy + l // 2, lux + l // 2], [rdy, rdx], arr)
