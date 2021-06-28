#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

// 파라미터로 주어지는 문자열은 const로 주어집니다. 변경하려면 문자열을 복사해서 사용하세요.
// skill_trees_len은 배열 skill_trees의 길이입니다.


int chkPossible(const char* skill, const char* tree, int l)
{
    int lt = 0; // 확인할 skill tree의 길이
    int idx = 1; // 순서 저장
    int val;
    int flag = 0; // 0을 만난적이 있는지 확인
    while (tree[lt] != '\0')
        lt++;
    int* compare = (int*)malloc(sizeof(int) * l);
    for (int i = 0; i < l; i++)
        compare[i] = 0;
    for (int i = 0; i < lt; i++)
    {
        for (int j = 0; j < l; j++)
        {
            if (tree[i] == skill[j])
            {
                compare[j] = idx;
                idx++;
            }
        }
    }
    val = compare[0];
    if (val == 0)
    {
        for (int i = 1; i < l; i++)
        {
            if (compare[i] != 0)
                return 0;
        }
        return 1;
    }
    for (int i = 1; i < l; i++)
    {
        if (compare[i] == 0)
        {
            flag = 1;
        }
        else
        {
            if (flag == 1)
                return 0;
            if (val > compare[i])
                return 0;
            val = compare[i];
        }
    }
    return 1;
}


int solution(const char* skill, const char* skill_trees[], size_t skill_trees_len) {
    int answer = 0;
    int ls = 0;
    while (skill[ls] != '\0')
        ls++;
    for (int i = 0; i < skill_trees_len; i++)
        answer += chkPossible(skill, skill_trees[i], ls);
    return answer;
}
