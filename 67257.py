from itertools import permutations
from copy import deepcopy


def solution(expression):
    answer = 0
    signs = []
    if '+' in expression:
        signs.append('+')
    if '-' in expression:
        signs.append('-')
    if '*' in expression:
        signs.append('*')
    cases = list(permutations(signs, len(signs)))
    for case in cases:
        tmp = getResult(case, expression)
        if answer <= tmp:
            answer = tmp
    return answer


def getResult(case, experession):
    tmp = ''
    nList = []
    for i in range(len(experession)):
        if experession[i] == '+' or experession[i] == '-' or experession[i] == '*':
            nList.append(int(tmp))
            nList.append(experession[i])
            tmp = ''
        else:
            tmp += experession[i]
    nList.append(int(tmp))
    stack = [nList[0]]
    for pSign in case: # 우선순위 sign부터 먼저 정리해준다
        for i in range(1, len(nList)):
            if nList[i] == '-' or nList[i] == '+' or nList[i] == '*':
                stack.append(nList[i])
            else:
                if stack[-1] == pSign: # 우선순위 sign인 경우 계산해준다
                    stack.pop()
                    lastNum = stack.pop()
                    if pSign == '+':
                        stack.append(lastNum + nList[i])
                    if pSign == '-':
                        stack.append(lastNum - nList[i])
                    if pSign == '*':
                        stack.append(lastNum * nList[i])
                else:
                    stack.append(nList[i])
        nList = deepcopy(stack)
        stack = [nList[0]]
    return abs(stack[0])
