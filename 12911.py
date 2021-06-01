def solution(n):
    n = str(bin(n))
    n = n[2:]
    ansList = [n[i] for i in range(len(n))]
    flag = 0
    cnt1 = 0
    cIdx = -1 # 0을 1로 바꿔줘야할 idx
    for i in range(len(n) - 1, -1, -1):
        if ansList[i] == '1':
            flag = 1
            cnt1 += 1
        if ansList[i] == '0' and flag == 1:
            cIdx = i
            break
    if cIdx != -1: # 자릿수 추가 불필요
        ansList[cIdx] = '1'
        for i in range(cIdx + 1, len(n)):
            ansList[i] = '0'
        for i in range(len(n) - 1, len(n) - cnt1, - 1):
            ansList[i] = '1'
    else:
        ansList = ['0'] * (len(n) + 1)
        ansList[0] = '1'
        for i in range(len(n), len(n) + 1 - cnt1, -1):
            ansList[i] = '1'
    ans = 0
    l = len(ansList)
    for i in range(l):
        if ansList[l - i - 1] == '1':
            ans += pow(2, i)
    return ans
