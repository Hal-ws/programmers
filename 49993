def solution(skill, skill_trees):
    l = len(skill_trees)
    answer = 0
    for i in range(l):
        answer += possiblechk(skill, skill_trees[i])
    return answer


def possiblechk(skill, chking):
    l = len(skill)
    ans = []
    for i in range(l):
        try:
            ans.append([i, chking.index(skill[i])])
        except Exception as e:
            pass
    l = len(ans)
    for i in range(1, l):
        if ans[i - 1][1] > ans[i][1]:
            return 0
    for i in range(l):
        if ans[i][0] != i:
            return 0
    return 1
