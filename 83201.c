#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

// scores_rows는 2차원 배열 scores의 행 길이, scores_cols는 2차원 배열 scores의 열 길이입니다.
char* solution(int** scores, size_t scores_rows, size_t scores_cols) {
    // return 값은 malloc 등 동적 할당을 사용해주세요. 할당 길이는 상황에 맞게 변경해주세요.
    char* answer = (char*)malloc(scores_rows * sizeof(char) + 1);
    for(int j = 0; j < scores_cols; j++)
    {
        int maxScore = -1;
        int minScore = 101;
        int sumScore = 0;
        int selfScore;
        double avgScore;
        for(int i = 0; i < scores_rows; i++)
        {
            if (i == j) // 자기자신의 평가
                selfScore = scores[i][j];
            else
            {
                if (scores[i][j] < minScore)
                    minScore = scores[i][j];
                if (scores[i][j] > maxScore)
                    maxScore = scores[i][j];
            }
            sumScore += scores[i][j];
        }
        if (minScore <= selfScore && selfScore <= maxScore)
            avgScore = sumScore / scores_rows;
        else
            avgScore = (sumScore - selfScore) / (scores_rows - 1);
        if (avgScore >= 90)
            answer[j] = 'A';
        else if (avgScore >= 80)
            answer[j] = 'B';
        else if (avgScore >= 70)
            answer[j] = 'C';
        else if (avgScore >= 50)
            answer[j] = 'D';
        else
            answer[j] = 'F';       
    }
    answer[scores_rows] = '\0';
    return answer;
}
