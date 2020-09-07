def solution(number, k):
    l1 = len(number)
    numList, answer, answerl = [], '', 0
    for i in range(l1):
        numList.append(int(number[i]))
    l2 = l1 - k
    start = 0
    while answerl < l2:
        print('numList[start:start + k + 1]: %s' %numList[start:start + k + 1])
        idx = start + numList[start:start + k + 1].index(max(numList[start:start + k + 1]))
        start = idx + 1
        answer += str(numList[idx])
        answerl += 1
        k -= idx - answerl
        print('numList: %s, start: %s, idx: %s k: %s' % (numList, start, idx, k))
        print('answer: %s' % answer)
        print('----------------------------------')
    print(answer)

    return answer

solution("1231234", 3)
