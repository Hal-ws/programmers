#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>


void cpt(int** arr, int y1, int x1, int y2, int x2, int* answer)
{
    int flag = 1;
    int std = arr[y1][x1];
    int yMid, xMid;
    yMid = (y1 + y2) / 2;
    xMid = (x1 + x2) / 2;
    for (int i = y1; i <= y2; i++)
    {
        for (int j = x1; j <= x2; j++)
        {
            if (arr[i][j] != std)
            {
                flag = 0;
                break;
            }
        }
    }
    if (flag)
    {
        answer[std] += 1;
    }
    else
    {
        cpt(arr, y1, x1, yMid, xMid, answer);
        cpt(arr, y1, xMid + 1, yMid, x2, answer);
        cpt(arr, yMid + 1, x1, y2, xMid, answer);
        cpt(arr, yMid + 1, xMid + 1, y2, x2, answer);
    }
    return;
}

// arr_rows는 2차원 배열 arr의 행 길이, arr_cols는 2차원 배열 arr의 열 길이입니다.
int* solution(int** arr, size_t arr_rows, size_t arr_cols) {
    // return 값은 malloc 등 동적 할당을 사용해주세요. 할당 길이는 상황에 맞게 변경해주세요.
    int* answer = (int*)malloc(sizeof(int) * 2);
    answer[0] = 0, answer[1] = 0;
    cpt(arr, 0, 0, arr_rows - 1, arr_cols - 1, answer);
    return answer;
}
