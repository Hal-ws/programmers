#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

int solution(int n) {
    int answer = 0;
    int num, digit;
    int* nList;
    num = n;
    digit = 0;
    while(num > 0)
    {
        num = num / 3;
        digit++;
    }
    nList = (int*)malloc(sizeof(int) * digit);
    for(int i = 0; i < digit; i++)
    {
        nList[i] = n % 3;
        n = n / 3;
    }
    for(int i = 0; i < digit; i++)
        answer += (nList[digit - i - 1] * getpow(i));
    return answer;
}


int getpow(b)
{
    int a = 1;
    if (b == 0)
        return 1;
    for(int i = 0; i < b; i++)
        a *= 3;
    return a;
}
