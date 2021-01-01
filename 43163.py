from collections import deque


def solution(begin, target, words):
    global stdLen
    answer = 0
    stdLen = len(begin)
    q = deque()
    q.append([begin, 0])
    visit = [0] * len(words)
    while len(q) > 0:
        cur = q[0][0]
        cnt = q[0][1]
        if cur == target:
            answer = cnt
            break
        for i in range(len(words)):
            if visit[i] == 0 and chk(cur, words[i]):
                visit[i] = 1
                q.append([words[i], cnt + 1])
        q.popleft()
    return answer


def chk(word1, word2):
    global stdLen
    cnt = 0
    for i in range(stdLen):
        if word1[i] == word2[i]:
            cnt += 1
    if cnt == stdLen - 1:
        return 1
    return 0
