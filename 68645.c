#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

int* solution(int n) {
    // return 값은 malloc 등 동적 할당을 사용해주세요. 할당 길이는 상황에 맞게 변경해주세요.
    int val = 1;
    int maxCnt = n * (n + 1) / 2;
    int dy[3] = {1, 0, -1};
    int dx[3] = {-1, 2, -1};
    int height = n;
    int width = 2 * n - 1;
    int* answer = (int*)malloc(sizeof(int) * (n * (n + 1) / 2));
    int** arr;
    int y = -1;
    int x = width / 2 + 1;
    int ny, nx;
    int d = 0;
    int idx = 0;
    arr = (int**)malloc(sizeof(int*) * height);
    for (int i = 0; i < height; i++) {
        arr[i] = (int*)malloc(sizeof(int) * width);
    }
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
            arr[i][j] = 0;
    }
    while (val <= maxCnt)
    {
        ny = y + dy[d];
        nx = x + dx[d];
        if (0 <= ny && ny < height && 0 <= nx && nx < width && arr[ny][nx] == 0)
        {
            arr[ny][nx] = val;
            y = ny;
            x = nx;
            val++;
        }
        else
            d = (d + 1) % 3;
    }
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            if (arr[i][j] != 0)
            {
                answer[idx] = arr[i][j];
                idx++;
            }
        }
    }
    return answer;
}
