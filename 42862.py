def solution(n, lost, reserve):
    students = [1] * n
    for i in range(len(lost)):
        students[lost[i] - 1] -= 1
    for i in range(len(reserve)):
        students[reserve[i] - 1] += 1
    answer = n
    for i in range(n):
        if students[i] == 0:
            if i == 0:
                if students[i + 1] > 1:
                    students[i] = 1
                    students[i + 1] -= 1
                else:
                    answer -= 1
            elif i == n - 1:
                if students[i - 1] > 1:
                    students[i] = 1
                    students[i - 1] -= 1
                else:
                    answer -= 1
            else:
                if students[i - 1] > 1 and students[i + 1] <= 1:
                    students[i - 1] -= 1
                    students[i] += 1
                elif students[i - 1] <= 1 and students[i + 1] > 1:
                    students[i + 1] -= 1
                    students[i] += 1
                elif students[i - 1] > 1 and students[i + 1] > 1:
                    students[i - 1] -= 1
                    students[i] += 1
                else:
                    answer -= 1
    return answer
