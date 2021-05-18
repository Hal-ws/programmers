def solution(numbers):
    answer = ''
    for i in range(len(numbers)):
        numbers[i] = str(numbers[i])
    numList = [[] for i in range(10)] # 0으로 시작~9로 시작
    for num in numbers:
        numList[int(num[0])].append(num)
    for i in range(10):
        if len(numList[i]) > 0:
            numList[i] = numSorting(numList[i])
    for i in range(9, -1, -1):
        for j in range(len(numList[i])):
            answer += numList[i][j]
    if answer[0] == '0':
        answer = '0'
    return answer


def numSorting(nums):
    maxL = 0
    stdNum = nums[0][0]
    for i in range(len(nums)):
        tmpL = len(nums[i])
        nums[i] = [nums[i], tmpL]
        if maxL < tmpL:
            maxL = tmpL
    for i in range(len(nums)):
        nums[i][0] += stdNum * (maxL - nums[i][1])
    nums.sort(reverse=True)
    for i in range(len(nums)):
        nums[i] = nums[i][0][:nums[i][1]]
    return nums
