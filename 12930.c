#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>


// 파라미터로 주어지는 문자열은 const로 주어집니다. 변경하려면 문자열을 복사해서 사용하세요.
char* solution(const char* s) {
    // return 값은 malloc 등 동적 할당을 사용해주세요. 할당 길이는 상황에 맞게 변경해주세요.
    int l = 0;
    int sIdx = 0;
    while (true)
    {
        if (s[l] == '\0')
            break;
        l++;
    }
    char* answer = (char*)malloc(sizeof(char) * l + 1);
    for (int i = 0; i < l; i++)
    {
        if (s[i] == ' ')
        {
            sIdx = i + 1;
            answer[i] = s[i];
        }
        else
        {
            if ((i - sIdx) % 2 == 0) // 대문자로 변환
            {
                if (s[i] >= 'a' && s[i] <= 'z')
                    answer[i] = s[i] - 32;
                else
                    answer[i] = s[i];
            }
            else // 소문자로 변환
            {
                if (s[i] >= 'A' && s[i] <= 'Z')
                    answer[i] = s[i] + 32;
                else
                    answer[i] = s[i];
            }
        }
    }
    answer[l] = '\0';
    return answer;
}
