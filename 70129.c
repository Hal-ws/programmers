#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

// 파라미터로 주어지는 문자열은 const로 주어집니다. 변경하려면 문자열을 복사해서 사용하세요.
int* solution(const char* s) {
    // return 값은 malloc 등 동적 할당을 사용해주세요. 할당 길이는 상황에 맞게 변경해주세요.
    int* answer = (int*)malloc(sizeof(int) * 2);
    int l = 0;
    int zCnt;
    int tmpL;
    int tmpL2;
    int tmp;
    char* newS;
    while (s[l] != '\0')
        l++;
    newS = (char*)malloc(sizeof(char) * l + 1);
    for (int i = 0; i < l; i++)
        newS[i] = s[i];
    newS[l] = '\0';
    answer[0] = 0;
    answer[1] = 0;
    while (true)
    {
        zCnt = 0;
        if (l == 1)
            break;
        for (int i = 0; i < l; i++)
        {
            if (newS[i] == '0')
                zCnt++;
        }
        tmpL = l - zCnt;
        tmpL2 = tmpL;
        l = 0;
        while (tmpL > 0)
        {
            tmpL = tmpL / 2;
            l++;
        }
        newS = (char*)malloc(sizeof(char) * l + 1);
        newS[l] = '\0';
        for (int i = l - 1; i >= 1; i--)
        {
            tmp = tmpL2 % 2;
            if (tmp == 0)
                newS[i] = '0';
            else
                newS[i] = '1';
            tmpL2 = tmpL2 / 2;
        }
        newS[0] = '1';
        answer[0] += 1;
        answer[1] += zCnt;
    }
    return answer;
}
