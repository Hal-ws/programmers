#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

// 파라미터로 주어지는 문자열은 const로 주어집니다. 변경하려면 문자열을 복사해서 사용하세요.
bool solution(const char* s) {
    int idx;
    bool answer = true;
    char stack[100001];
    idx = 0;
    int i = 0;
    while(true)
    {
        if (s[i] == '(')
        {
            stack[idx] = '(';
            idx++;
        }
        else
        {
            if (idx == 0)
                return false;
            if (stack[idx - 1] == '(')
            {
                stack[idx - 1] = ' ';
                idx--;
            }
        }
        i++;
        if (s[i] == '\0')
            break;
    }
    if (idx == 0)
        return true;
    else
        return false;
    return answer;
}
