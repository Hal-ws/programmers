import heapq


def solution(A, B):
    answer = 0
    aList, bList = [], []
    for i in range(len(A)):
        heapq.heappush(aList, A[i])
        heapq.heappush(bList, B[i])
    while 1:
        pA, pB = aList[0], bList[0]
        if pA < pB:
            answer += 1
            heapq.heappop(aList)
            heapq.heappop(bList)
        else:
            heapq.heappop(bList)
        if len(aList) == 0 or len(bList) == 0:
            break
    return answer
