from collections import deque
import heapq


def solution(jobs):
    jobs.sort()
    totalT = 0
    q = deque()
    waiting = []
    for tmp in jobs:
        q.append([tmp[0], tmp[1]]) # 시작시간, 작업시간 순으로 정리
    first = q.popleft()
    totalT += first[1]
    curT = first[0] + first[1] # 가장 최근에 처리중인 작업을 종료하는 시간
    while len(q) + len(waiting) != 0: # q 도 비고 waiting 도 다 처리해야 종료
        while len(q) > 0:
            sT = q[0][0]
            if sT < curT: # waiting에 추가해줘야함
                tmp = q.popleft()
                heapq.heappush(waiting, [tmp[1], tmp[0]])
            else:
                break
        if len(waiting) == 0: # 현재 대기중인 작업이 없음. 바로 q의 제일 앞에 있는 작업 수행
            tmp = q.popleft()
            sT, wT = tmp[0], tmp[1]
            totalT += wT
            curT = sT + wT
        else: # 대기중인 작업 있으므로 그 작업부터 처리
            tmp = heapq.heappop(waiting)
            sT, wT = tmp[1], tmp[0]
            totalT += (curT - sT) + wT
            curT = curT + wT
    answer = totalT // len(jobs)
    return answer
