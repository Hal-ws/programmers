def solution(nums):
    answer = 0
    maxChoice = len(nums) // 2
    ponketBook = {}
    for i in range(len(nums)):
        if nums[i] not in ponketBook:
            ponketBook[nums[i]] = 1
            answer += 1
        if answer == maxChoice:
            break
    return answer
