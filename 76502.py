from _collections import deque


def solution(s):
    answer = 0
    l = len(s)
    q = deque()
    for i in range(l):
        q.append(s[i])
    for x in range(l):
        answer += rightChk(q)
        q.append(q.popleft())
    return answer


def rightChk(q):
    stack = []
    for i in range(len(q)):
        stack.append(q[i])
        if len(stack) > 1:
            if stack[-2] == '(' and stack[-1] == ')':
                stack.pop()
                stack.pop()
            elif stack[-2] == '{' and stack[-1] == '}':
                stack.pop()
                stack.pop()
            elif stack[-2] == '[' and stack[-1] == ']':
                stack.pop()
                stack.pop()
    if len(stack) == 0:
        return 1
    else:
        return 0
