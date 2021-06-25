#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

char* solution(int n) {
    // 리턴할 값은 메모리를 동적 할당해주세요.
    char* answer;
    answer = (char*)malloc(sizeof(char) * 3 * n + 1);
    answer[0] = 0;
    for (int i = 0; i < n; i++)
    {
        if (i % 2) // 홀수
            strcat(answer, "박");
        else
            strcat(answer, "수");
    }
    answer[3 * n] = '\0';
    return answer;
}
