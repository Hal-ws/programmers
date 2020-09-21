def solution(scoville, K):
    ls, scoville, answer, endflag = len(scoville), sorted(scoville), 0, 0
    for i in range(ls - 1):
        if scoville[i] < K:
            if scoville[i] <= scoville[i + 1]:
                scoville[i + 1] = scoville[i] + scoville[i + 1] * 2
            else:
                scoville[i + 1] = scoville[i] * 2 + scoville[i + 1]
            answer += 1
            scoville[i] = None
            print(scoville)
        else:
            break
        if scoville[i + 1] >= K:
            return answer
    return -1
