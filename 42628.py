from queue import PriorityQueue


def solution(operations):
    global maxQ, minQ, memory
    answer = [0, 0]
    maxQ = PriorityQueue()
    minQ = PriorityQueue()
    memory = {}
    for c in operations:
        process(c)
    while maxQ.empty() != True:
        tmpV = -1 * maxQ.get()
        if memory[tmpV] > 0:
            answer[0] = tmpV
            break
    while minQ.empty() != True:
        tmpV = minQ.get()
        if memory[tmpV] > 0:
            answer[1] = tmpV
            break
    return answer


def process(c):
    global maxQ, minQ, memory
    v1, v2 = map(str, c.split())
    v2 = int(v2)
    if v1 == 'I': # 삽입
        maxQ.put(-v2)
        minQ.put(v2)
        if memory.get(v2) == None:
            memory[v2] = 1
        else:
            memory[v2] += 1
    else:
        if v2 == 1: # 최대값 삭제
            while maxQ.empty() != True:
                tmpV = -1 * maxQ.get() #현재 최대값
                if memory[tmpV] > 0: # 저장된 tmpV가 있음
                    memory[tmpV] -= 1
                    break
        else: #최소값 삭제
            while minQ.empty() != True:
                tmpV = minQ.get()
                if memory[tmpV] > 0:
                    memory[tmpV] -= 1
                    break
