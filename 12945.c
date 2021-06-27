#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

int solution(int n) {
    int answer = 0;
    int fibo[3] = { 0, 1, 1 };
    if (n == 2)
        return 1;
    for (int i = 0; i < n - 2; i++)
    {
        fibo[0] = fibo[1];
        fibo[1] = fibo[2];
        fibo[2] = (fibo[0] + fibo[1]) % 1234567;
    }
    return fibo[2];
}
