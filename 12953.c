#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

// arr_len은 배열 arr의 길이입니다.
int solution(int arr[], size_t arr_len) {
    int answer = 0;
    for (int i = 1; i < arr_len; i++)
    {
        arr[i] = lcd(arr[i - 1], arr[i]);
    }
    return arr[arr_len - 1];
}

int lcd(int a, int b)
{
    return (a * b) / gcd(a, b);
}


int gcd(int a, int b)
{
    int r;
    while (b != 0)
    {
        r = a % b;
        a = b;
        b = r;
    }
    return a;
}
