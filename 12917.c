#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

// 파라미터로 주어지는 문자열은 const로 주어집니다. 변경하려면 문자열을 복사해서 사용하세요.
char* solution(const char* s) {
    // return 값은 malloc 등 동적 할당을 사용해주세요. 할당 길이는 상황에 맞게 변경해주세요.
    int cnt = 0;
    int aIdx = 0;
    int i = 122;
    while (1)
    {
        if(s[cnt] == '\0')
            break;
        cnt++;
    }
    char* answer = (char*)malloc(sizeof(char) * cnt + 1);
    answer[cnt] = '\0';
    while (i >= 65)
    {
        for(int j = 0; j < cnt; j++)
        {
            if (s[j] == i)
            {
                answer[aIdx] = i;
                aIdx++;
            }
        }
        i--;
        if(i == 96)
            i = 90;
    }
    return answer;
}
