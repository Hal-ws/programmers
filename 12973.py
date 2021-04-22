def solution(s):
    stack = []
    for w in s:
        stack.append(w)
        if len(stack) >= 2:
            while 1:
                if stack[-1] == stack[-2]:
                    stack.pop()
                    stack.pop()
                else:
                    break
                if len(stack) < 2:
                    break
    if len(stack) == 0:
        return 1
    else:
        return 0
