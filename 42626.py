import heapq


def solution(scoville, K):
    answer = -1
    heap = []
    cnt = 0
    for scv in scoville:
        heapq.heappush(heap, scv)
    while 1:
        first = heapq.heappop(heap)
        if first >= K:
            answer = cnt
            break
        if len(heap) == 0:
            return -1
        second = heapq.heappop(heap)
        mixed = first + (second * 2)
        heapq.heappush(heap, mixed)
        cnt += 1
    return answer
