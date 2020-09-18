def solution(genres, plays):
    lp = len(plays)
    for i in range(lp):
        plays[i] = [genres[i], plays[i], i]
    plays.sort()
    classicSum = [[None, None]]
    j = 0
    for i in range(lp):
        if plays[i][0] != classicSum[j][1]:
            classicSum.append([plays[i][1], plays[i][0]])
            j += 1
        else:
            classicSum[j][0] += plays[i][1]
    classicSum = sorted(classicSum[1:len(classicSum)], reverse=True)
    firstGenre, secondGenre = [], []
    for i in range(lp):
        if plays[i][0] == classicSum[0][1]:
            firstGenre.append([plays[i][1], plays[i][2]])
        if plays[i][0] == classicSum[1][1]:
            secondGenre.append([plays[i][1], plays[i][2]])
    firstGenre, secondGenre = sorted(firstGenre, reverse=True), sorted(secondGenre, reverse=True)
    print('firstGenre: %s' %firstGenre)
    print('secondGenre: %s' %secondGenre)
    l1, l2, cnt, answer = len(firstGenre), len(secondGenre), 0, []
    for i in range(1, l1):
        if firstGenre[i][0] < firstGenre[i - 1][0]:
            answer.append(firstGenre[i - 1][1])
            cnt += 1
        if cnt == 2:
            break
    if cnt == 0:
        answer.append(firstGenre[l1 - 1][1])
        answer.append(firstGenre[l1 - 2][1])
    elif cnt == 1:
        answer.append(firstGenre[l1 - 1][1])
    cnt = 2
    for i in range(1, l2):
        if secondGenre[i][0] < secondGenre[i - 1][0]:
            answer.append(secondGenre[i - 1][1])
            cnt += 1
        if cnt == 4:
            break
    if cnt == 2:
        answer.append(secondGenre[l2 - 1][1])
        answer.append(secondGenre[l2 - 2][1])
    if cnt == 3:
        answer.append(secondGenre[l2 - 1][1])
    print(answer)
    return answer

solution(["classic", "pop", "classic", "classic", "pop"], [1000, 1000, 1000, 1000, 1000])
