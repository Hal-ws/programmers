#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

// 파라미터로 주어지는 문자열은 const로 주어집니다. 변경하려면 문자열을 복사해서 사용하세요.
int solution(const char* dirs) {
    int answer = 0;
    int i = 0;
    int y, x;
    int board[11][11][11][11] = {0, };
    y = 5;
    x = 5;
    while (dirs[i] != '\0')
    {
        if (dirs[i] == 'U' && y > 0)
        {
            board[y][x][y - 1][x] = 1;
            board[y - 1][x][y][x] = 1;
            y--;
        }
        if (dirs[i] == 'D' && y < 10)
        {
            board[y][x][y + 1][x] = 1;
            board[y + 1][x][y][x] = 1;
            y++;
        }   
        if (dirs[i] == 'L' && x > 0)
        {
            board[y][x][y][x - 1] = 1;
            board[y][x - 1][y][x] = 1;
            x--;
        }   
        if (dirs[i] == 'R' && x < 10)
        {
            board[y][x][y][x + 1] = 1;
            board[y][x + 1][y][x] = 1;
            x++;
        }
        i++;
    }
    for (int i = 0; i < 11; i++)
    {
        for (int j = 0; j < 11; j++)
        {
            for(int k = 0; k < 11; k++)
            {
                for (int l = 0; l < 11; l++)
                    answer += board[i][j][k][l];
            }
        }
    }
    return answer / 2;
}
