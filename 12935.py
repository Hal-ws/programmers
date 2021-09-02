def solution(arr):
    minVal = None
    for num in arr:
        if minVal == None or num < minVal:
            minVal = num
    del arr[arr.index(minVal)]
    if len(arr) == 0:
        arr = [-1]
    return arr
