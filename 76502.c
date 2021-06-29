#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>


// 파라미터로 주어지는 문자열은 const로 주어집니다. 변경하려면 문자열을 복사해서 사용하세요.
int solution(const char* s) {
    int answer = 0;
    int l = 0;
    char tmp;
    int flag, idx;

    while (s[l] != '\0')
        l++;
    char* newS = (char*)malloc(sizeof(char) * l + 1);
    newS[l] = '\0';
    for (int i = 0; i < l; i++)
        newS[i] = s[i];
    for (int i = 0; i < l; i++)
    {
        // 올바른 괄호인지 확인
        printf("newS: %s\n", newS);
        flag = 1;
        idx = 1;
        char* stack = (char*)malloc(sizeof(char) * l + 1);
        stack[l] = '\0';
        stack[0] = newS[0];
        if (stack[0] == ')' || stack[0] == ']' || stack[0] == '}')
            flag = 0;
        else
        {
            for (int j = 1; j < l; j++)
            {
                if (newS[j] == '(' || newS[j] == '{' || newS[j] == '[')
                {
                    stack[idx] = newS[j];
                    idx++;
                }
                else
                {
                    if (idx == 0)
                    {
                        flag = 0;
                        break;
                    }
                    if (newS[j] == ')')
                    {
                        if (stack[idx - 1] != '(')
                        {
                            flag = 0;
                            break;
                        }
                        else
                        {
                            stack[idx - 1] = ' ';
                            idx--;
                        }
                    }
                    if (newS[j] == '}')
                    {
                        if (stack[idx - 1] != '{')
                        {
                            flag = 0;
                            break;
                        }
                        else
                        {
                            stack[idx - 1] = ' ';
                            idx--;
                        }
                    }
                    if (newS[j] == ']')
                        if (stack[idx - 1] != '[')
                        {
                            flag = 0;
                            break;
                        }
                        else
                        {
                            stack[idx - 1] = ' ';
                            idx--;
                        }
                }
            }
        }
        if (stack[0] != ' ')
            flag = 0;
        answer += flag;
        // 회전
        tmp = newS[0];
        for (int j = 0; j < l; j++)
            newS[j] = newS[j + 1];
        newS[l - 1] = tmp;
    }
    return answer;
}
