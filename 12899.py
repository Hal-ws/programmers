def solution(n):
    digit = 1
    numList = []
    answer = ''
    while 1:
        if 3 * (pow(3, digit - 1) - 1) // 2 <= n <= 3 * (pow(3, digit) - 1) // 2:
            break
        digit += 1
    while digit > 0:
        num = n // pow(3, digit - 1)
        n -= num * pow(3, digit - 1)
        if digit > 1:
            minNxt = (pow(3, digit - 1) - 1) // 2
            if n < minNxt:
                num -= 1
                n += pow(3, digit - 1)
        numList.append(num)
        digit -= 1
    for i in range(len(numList)):
        if numList[i] == 3:
            numList[i] = '4'
        else:
            numList[i] = str(numList[i])
        answer += numList[i]
    return answer
