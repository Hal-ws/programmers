def solution(s):
    cnt = 1
    delCnt = 0
    while 1:
        zCnt = 0
        for i in range(len(s)):
            if s[i] == '0':
                zCnt += 1
                delCnt += 1
        s = '1' * (len(s) - zCnt)
        s = bin(len(s))
        s = s[2:]
        if s == '1':
            break
        cnt += 1
    return [cnt, delCnt]


print(solution('1' * 150000))
