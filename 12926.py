def solution(s, n):
    answer = ''
    for c in s:
        if 'a' <= c <= 'z':  # 소문자. ord값 97 ~ 122
            if ord(c) + n <= 122:
                answer += chr(ord(c) + n)
            else:
                newIdx = (ord(c) + n) % 122 + 96
                answer += chr(newIdx)
        elif 'A' <= c <= 'Z': #대문자. ord값 65 ~ 90
            if ord(c) + n <= 90:
                answer += chr(ord(c) + n)
            else:
                newIdx = (ord(c) + n) % 90 + 64
                answer += chr(newIdx)
        else:
            answer += c
    return answer
