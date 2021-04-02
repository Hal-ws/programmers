def solution(sticker):
    if len(sticker) == 1 or len(sticker) == 2:
        return max(sticker)
    dp1, dp2 = [0, sticker[0]], [0, sticker[1]] # 0번 스티커를 포함
    for i in range(1, len(sticker) - 1): # 마지막 스티커는 포함못함
        dp1.append(max(dp1[i - 1] + sticker[i], dp1[i]))
    for i in range(2, len(sticker)):
        dp2.append(max(dp2[i - 2] + sticker[i], dp2[i - 1]))
    return max(dp1[-1], dp2[-1])
