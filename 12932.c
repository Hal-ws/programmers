#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

int* solution(long long n) {
    // 리턴할 값은 메모리를 동적 할당해주세요.
    int digit = 0;
    long long x = n;
    int tmpVal;
    while(true)
    {
        digit++;
        x = x / 10;
        if(x == 0)
            break;
    }
    int* answer = (int*)malloc(sizeof(int) * digit);
    for(int i = 0; i < digit; i++)
    {
        tmpVal = n % 10;
        n = n / 10;
        answer[i] = tmpVal;
    }
    
    
    return answer;
}
