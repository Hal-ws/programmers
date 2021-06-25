#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

long long solution(long long n) {
    int maxCnt = 7071068;
    long long compare;
    for (long long i = 1; i < maxCnt; i++)
    {
        compare = i * i;
        if (compare == n)
            return (i + 1) * (i + 1);
        if (i == n)
            break;
    }
    return -1;
}
