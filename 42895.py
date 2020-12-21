def solution(N, number):
    dp = [[] for i in range(9)]
    answer = 0
    dp[1].append(N)
    for i in range(2, 9):
        dp[i].append(dp[i - 1][0] * 10 + N)
    for i in range(1, 9):
        answer += 1
        endflag = 0
        if dp[i][0] == number:
            return i
        for size in range(1, i // 2 + 1):
            for num1 in dp[size]:
                for num2 in dp[i - size]:
                    tmp = num1 + num2
                    if tmp not in dp[i]:
                        dp[i].append(tmp)
                        if tmp == number:
                            endflag = 1
                    tmp = num1 - num2
                    if tmp not in dp[i]:
                        dp[i].append(tmp)
                        if tmp == number:
                            endflag = 1
                    tmp = num2 - num1
                    if tmp not in dp[i]:
                        dp[i].append(tmp)
                        if tmp == number:
                            endflag = 1
                    if num1 != 0:
                        tmp = num2 // num1
                        if tmp not in dp[i]:
                            dp[i].append(tmp)
                            if tmp == number:
                                endflag = 1
                    if num2 != 0:
                        tmp = num1 // num2
                        if tmp not in dp[i]:
                            dp[i].append(tmp)
                            if tmp == number:
                                endflag = 1
                    tmp = num1 * num2
                    if tmp not in dp[i]:
                        dp[i].append(tmp)
                        if tmp == number:
                            endflag = 1
        if endflag:
            break
    if endflag:
        return answer
    else:
        return -1
