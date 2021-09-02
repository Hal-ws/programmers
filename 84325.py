def solution(table, languages, preference):
    maxScore = 0
    answer = ''
    jobList = []
    for i in range(5):
        table[i] = list(map(str, table[i].split()))
    for i in range(5):
        jobList.append(table[i][0])
    for i in range(5):
        tmpScore = getscore(table, i, languages, preference)
        if tmpScore > maxScore:
            maxScore = tmpScore
            answer = jobList[i]
        elif tmpScore == maxScore:
            answer = min(jobList[i], answer)
    return answer


def getscore(table, jobIdx, languages, preference):
    result = 0 ## job으로 얻을 수 있는 점수
    for i in range(len(languages)): # 사용 언어
        for j in range(1, 6):
            if table[jobIdx][j] == languages[i]: # 해당 언어가 존재
                result += (preference[i] * (6 - j))
    return result
