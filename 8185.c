#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

// 파라미터로 주어지는 문자열은 const로 주어집니다. 변경하려면 문자열을 복사해서 사용하세요.
char* solution(const char* number, int k) {
    // return 값은 malloc 등 동적 할당을 사용해주세요. 할당 길이는 상황에 맞게 변경해주세요.
    int l = 0;
    int delCnt = 0;
    int idx = 0;
    int j;
    while (number[l] != '\0')
        l++;
    char* answer = (char*)malloc(sizeof(l - k) + 1);
    answer[0] = number[0];
    printf("answer, idx: %s, %d\n", answer, idx);
    for (int i = 1; i < l; i++)
    {
        if (delCnt == k) //더 못지움
        {
            if (idx == l - k - 1)
                break;
            answer[idx + 1] = number[i];
            idx++;
        }
        else // 삭제 가능할때
        {
            for (j = idx; j >= 0; j--) // 삭제 가능한 것부터 삭제하면서 진행
            {
                if (answer[j] < number[i] && delCnt < k) //j 에 있는걸 삭제가능
                {
                    answer[j] = ' ';
                    delCnt++;
                }
                else // 불가능하면 빠져나옴
                    break;
            }
            if (j + 1 < l - k)
                answer[j] = number[i];
            idx = j + 1;    
        }
        printf("answer, idx: %s, %d\n", answer, idx);
    }
    answer[l - k] = '\0';
    
    return answer;
}

int main(void)
{
    printf("%s", solution("0000", 2));
    return 0;
}
