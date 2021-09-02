def solution(arr):
    del arr[arr.index(min(arr))]
    if len(arr) == 0:
        arr = [-1]
    return arr
