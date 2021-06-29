#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

// queries_row_len은 2차원 배열 queries의 행(세로) 길이입니다.
// queries_col_len은 2차원 배열 queries의 열(가로) 길이입니다.
// queries[i][j]는 queries의 i번째 행의 j번째 열에 저장된 값을 의미합니다.
int* solution(int rows, int columns, int** queries, size_t queries_row_len, size_t queries_col_len) {
    int* answer = (int*)malloc(sizeof(int) * queries_row_len);
    int** arr;
    int val = 1;
    int y1, x1, y2, x2;
    int tmp, tmp2, minVal;
    arr = (int**)malloc(sizeof(int*) * rows);
    for (int i = 0; i < rows; i++)
        arr[i] = (int*)malloc(sizeof(int) * columns);
    for (int i = 0; i < rows; i++)
    {
        for (int j = 0; j < columns; j++)
        {
            arr[i][j] = val;
            val++;
        }
    }
    int* q;
    for (int i = 0; i < queries_row_len; i++)
    {
        q = queries[i];
        y1 = q[0] - 1;
        x1 = q[1] - 1;
        y2 = q[2] - 1;
        x2 = q[3] - 1;
        tmp = arr[y1][x1];
        minVal = tmp;
        for (int x = x1 + 1; x <= x2; x++)
        {
            tmp2 = arr[y1][x];
            arr[y1][x] = tmp;
            tmp = tmp2;
            if (tmp <= minVal)
                minVal = tmp;
        }
        for (int y = y1 + 1; y <= y2; y++)
        {
            tmp2 = arr[y][x2];
            arr[y][x2] = tmp;
            tmp = tmp2;
            if (tmp <= minVal)
                minVal = tmp;
        }
        for (int x = x2 - 1; x >= x1; x--)
        {
            tmp2 = arr[y2][x];
            arr[y2][x] = tmp;
            tmp = tmp2;
            if (tmp <= minVal)
                minVal = tmp;
        }
        for (int y = y2 - 1; y >= y1; y--)
        {
            tmp2 = arr[y][x1];
            arr[y][x1] = tmp;
            tmp = tmp2;
            if (tmp <= minVal)
                minVal = tmp;
        }
        answer[i] = minVal;
    }
    return answer;
}
