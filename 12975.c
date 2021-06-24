#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

// 파라미터로 주어지는 문자열은 const로 주어집니다. 변경하려면 문자열을 복사해서 사용하세요.
int main(void) {
    int answer = 0;
    int sign, flag, sIdx, cnt, nIdx;
    int* ps;
    char number[10];
    char s[10] = "+1234";
    ps = &s[0];
    flag = 0;
    nIdx = 0;
    for (cnt = 0; cnt < 10; cnt++)
    {
        if (s[cnt] == '\0')
        {
            printf("chk!\n");
            printf("cnt: %d\n", cnt);
            break;
        }
    }
    printf("cnt: %d\n", cnt);
    if (s[0] == '-')
    {
        sign = -1;
        flag = 1;
    }
    else
    {
        sign = 1;
        if (s[0] == '+')
            flag = 1;
    }
    if (flag)
        sIdx = 1;
    else
        sIdx = 0;
    for (sIdx; sIdx < cnt; sIdx++)
    {
        number[nIdx] = s[sIdx];
        nIdx++;
    }
    answer = sign * atoi(number);
    return answer;
}
