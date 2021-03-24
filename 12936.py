def solution(n, k):
    answer = getans([], k, [i + 1 for i in range(n)], n)
    return answer


def getans(ansList, k, numList, n):
    if len(ansList) == n:
        return ansList
    minusVal = factorial(len(numList) - 1)
    tmpVal = 0
    for i in range(len(numList)):
        tmpVal += minusVal
        if tmpVal >= k:
            tmpVal -= minusVal
            ansList.append(numList[i])
            del numList[i]
            return getans(ansList, k - tmpVal, numList, n)


def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


print(solution(3, 5))
