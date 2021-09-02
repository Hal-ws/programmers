def solution(arr1, arr2):
    w = len(arr1[0])
    h = len(arr1)
    answer = [[0 for j in range(w)] for i in range(h)]
    for j in range(w):
        for i in range(h):
            answer[i][j] = arr1[i][j] + arr2[i][j]
    return answer
