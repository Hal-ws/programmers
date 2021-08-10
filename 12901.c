#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

char* solution(int a, int b) {
    // 리턴할 값은 메모리를 동적 할당해주세요.
    int tDays = 0;
    int diff;
    char* answer = (char*)malloc(sizeof(char) * 3 + 1);
    for(int i = 1; i < a; i++)
    {
        if(i == 2)
            tDays += 29;
        else
        {
            if (i == 1 || i == 3 || i == 5 || i == 7 || i == 8 || i == 10)
                tDays += 31;
            else
                tDays += 30;
        }
    }
    tDays += (b - 1);
    diff = tDays % 7;
    if (diff == 0)
    {
        answer[0] = 'F';
        answer[1] = 'R';
        answer[2] = 'I';
    }
    if (diff == 1)
    {
        answer[0] = 'S';
        answer[1] = 'A';
        answer[2] = 'T';
    }
    if (diff == 2)
    {
        answer[0] = 'S';
        answer[1] = 'U';
        answer[2] = 'N';
    }
    if (diff == 3)
    {
        answer[0] = 'M';
        answer[1] = 'O';
        answer[2] = 'N';
    }
    if (diff == 4)
    {
        answer[0] = 'T';
        answer[1] = 'U';
        answer[2] = 'E';
    }
    if (diff == 5)
    {
        answer[0] = 'W';
        answer[1] = 'E';
        answer[2] = 'D';
    }
    if (diff == 6)
    {
        answer[0] = 'T';
        answer[1] = 'H';
        answer[2] = 'U';
    }
    answer[3] = '\0';
    return answer;
}
