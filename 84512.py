from itertools import product


def solution(word):
    wordBook = []
    for l in range(1, 6):
        wordBook += list(product(['A', 'E', 'I', 'O', 'U'], repeat = l))
    wordBook.sort()
    for i in range(len(wordBook)):
        tmp = ''
        for j in range(len(wordBook[i])):
            tmp += wordBook[i][j]
        wordBook[i] = tmp
    return wordBook.index(word) + 1
