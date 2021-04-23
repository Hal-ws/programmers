def solution(s):
    answer = ''
    for w in s:
        tmp = ord(w)
        if len(answer) == 0:
            if 97 <= tmp <= 122:
                tmp -= 32
            answer += chr(tmp)
        else:
            last = ord(answer[-1])
            if last == 32: # 빈칸 다음에 올때
                if 97 <= tmp <= 122:
                    tmp -= 32
                answer += chr(tmp)
            else:
                if 65 <= tmp <= 90:
                    tmp += 32
                answer += chr(tmp)
    return answer
