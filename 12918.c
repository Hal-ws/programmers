#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

// 파라미터로 주어지는 문자열은 const로 주어집니다. 변경하려면 문자열을 복사해서 사용하세요.
bool solution(const char* s) {
    int l = 0;
    for(int i = 0; i < 9; i++)
    {
        if(s[i] == '\0')
        {
            l = i;
            break;
        }
        if(s[i] != '0' && s[i] != '1' && s[i] != '2' && s[i] != '3' && s[i] != '4' && s[i] != '5' && s[i] != '6' && s[i] != '7' && s[i] != '8' && s[i] != '9')
            return false;
    }
    if(l == 4 || l == 6)
        return true;
    return false;
}
