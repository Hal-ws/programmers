#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

// nums_len은 배열 nums의 길이입니다.
int solution(int nums[], size_t nums_len) {
    int answer = 0;
    int i, j, k;
    for(i = 0; i < nums_len - 2; i++)
    {
        for(j = i + 1; j < nums_len - 1; j++)
        {
            for (k = j + 1; k < nums_len; k++)
            {
                if(chkSosu(nums[i] + nums[j] + nums[k]))
                    answer++;
            }
        }
    }
    return answer;
}

int chkSosu(int num)
{
    int i = 2;
    for (i; i < num; i++)
    {
        if(num % i == 0)
            return 0;
    }
    return 1;
}
