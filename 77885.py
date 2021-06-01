def solution(numbers):
    answer = []
    for num in numbers:
        i = 0
        while 1:
            if num == pow(2, i) - 1:
                if i == 0:
                    answer.append(1)
                else:
                    answer.append(pow(2, i) + pow(2, i - 1) - 1)
                break
            if num < pow(2, i) - 1:
                for j in range(i):
                    if num | pow(2, j) != num:
                        num = num | pow(2, j)
                        break
                if j >= 1:
                    num -= pow(2, j - 1)
                answer.append(num)
                break
            i += 1
    return answer
