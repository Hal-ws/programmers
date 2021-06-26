#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

int solution(int left, int right) {
    int answer = 0;
    for(int i = left; i <= right; i++)
    {
        if(chkeven(i)) // 짝수
            answer += i;
        else // 홀수
            answer -= i;
    }
    return answer;
}


int chkeven(int n)
{
    int cnt = 0;
    for(int i = 1; i <= n; i++)
    {
         if (n % i == 0)
             cnt++;
    }
    if (cnt % 2)
        return 0;
    else
        return 1;
}
