def solution(n,a,b):
    cnt = 1
    a, b = a + pow(2, n) - 2, b + pow(2, n) - 2
    while 1:
        a = (a - 1) // 2
        b = (b - 1) // 2
        if a == b:
            return cnt
        cnt += 1
    return cnt
