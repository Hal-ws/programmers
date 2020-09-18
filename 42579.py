def solution(genres, plays):
    lp = len(plays)
    for i in range(lp):
        plays[i] = [genres[i], plays[i], i]
    plays.sort()
    genreSum = [[None, None]]
    j = 0
    for i in range(lp):
        if plays[i][0] != genreSum[j][1]:
            genreSum.append([plays[i][1], plays[i][0]])
            j += 1
        else:
            genreSum[j][0] += plays[i][1]
    genreSum = sorted(genreSum[1:len(genreSum)], reverse=True)
    print('genreSum: %s' %genreSum)
    lg, answer = len(genreSum), []
    for i in range(lg):
        for j in range(lp):
            if genreSum[i][1] == plays[j][0]:
                start = j
                break
        for j in range(start, lp):
            if plays[j][0] != plays[start][0]:
                flag, end = 0, j
                break
            if j == lp - 1:
                flag, end = 1, lp
                break
        answer += choicetwosongs(sorted(plays[start:end], reverse=True), end - start)
    print(answer)
    return answer


def choicetwosongs(songs, l):
    if l == 1:
        return [songs[0][2]]
    flag, flag2, temp = 0, 0, []
    for i in range(1, l):
        if songs[i][1] < songs[i - 1][1]:
            flag = 1
            start = i
            break
    if flag:
        temp.append(songs[start - 1][2])
        if start > 2:
            temp.append(songs[start - 2][2])
        else:
            for j in range(start + 1, l):
                if songs[j] < songs[j - 1]:
                    flag2 = 1
                    break
            if flag2:
                temp.append(songs[j - 1][2])
            else:
                temp.append(songs[l - 1][2])
    else:
        temp.append(songs[l - 1][2])
        temp.append(songs[l - 2][2])
    return temp
solution(["classic", "classic", "classic", "classic", "pop"], [500, 150, 800, 800, 2500])
