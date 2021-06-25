#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

char* solution(int num) {
    // 리턴할 값은 메모리를 동적 할당해주세요
    char* answer;
    if(num % 2) // 홀수
    {
        answer = (char*)malloc(sizeof(char) * 4);
        answer[0] = 'O';
        answer[1] = 'd';
        answer[2] = 'd';
        answer[3] = '\0';
    }
    else // 짝수
    {
        answer = (char*)malloc(sizeof(char) * 5);
        answer[0] = 'E';
        answer[1] = 'v';
        answer[2] = 'e';
        answer[3] = 'n';
        answer[4] = '\0';
    }
        
    return answer;
}
