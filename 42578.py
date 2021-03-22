def solution(clothes):
    wears = {}
    type = set()
    answer = 1
    for c in clothes:
        n, t = c[0], c[1]
        if wears.get(t) == None:
            wears[t] = 1
        else:
            wears[t] += 1
        type.add(t)
    type = list(type)
    for t in type:
        answer *= (wears[t] + 1)
    return answer - 1
