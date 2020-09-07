def solution(number, k):
    l = len(number)
    numList, answer, answerl = [], '', 0
    for i in range(l):
        numList.append(int(number[i]))
    l = l - k
    while answerl < l:
        idx = numList[:k + 1].index(max(numList[:k + 1]))
        answer += str(numList[idx])
        answerl += 1
        k -= idx
        numList = numList[idx + 1:]
    return answer
