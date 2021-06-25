#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

int solution(int n) {
    int answer = 0;
    while(true)
    {
        answer += n % 10;
        n = n / 10;
        if(n == 0)
            break;
    }
    return answer;
}
