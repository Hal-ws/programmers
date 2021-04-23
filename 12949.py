def solution(arr1, arr2):
    h1, w1, h2, w2 = len(arr1), len(arr1[0]), len(arr2), len(arr2[0])
    answer = [[0 for j in range(w2)] for i in range(h1)]
    for i in range(h1):
        for j in range(w2):
            answer[i][j] = getComponent(i, j, arr1, arr2)
    return answer


def getComponent(y, x, arr1, arr2):
    result = 0
    for idx in range(len(arr1[0])):
        result += (arr1[y][idx] * arr2[idx][x])
    return result
