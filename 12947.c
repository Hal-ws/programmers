#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

bool solution(int x) {
    int digitSum = 0;;
    int num = x;
    while (true)
    {
        digitSum += (num % 10);
        num = num / 10;
        if (num == 0)
            break;
    }
    if (x % digitSum)
        return false;
    else
        return true;
}
