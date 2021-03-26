def solution(number, k):
    answer = ''
    stack = []
    cnt = 0
    for n in number:
        num = int(n)
        if cnt == k: # 더이상 못지움
            stack.append(num)
        else: # 지울 수 있음
            if len(stack) == 0:
                stack.append(num)
            else:
                while stack[-1] < num:
                    cnt += 1
                    stack.pop()
                    if cnt == k or len(stack) == 0:
                        break
                stack.append(num)
    for _ in range(k - cnt):
        stack.pop()
    for n in stack:
        answer += str(n)
    return answer
