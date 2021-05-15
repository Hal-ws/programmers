def solution(numbers, hand):
    answer = ''
    if hand == 'right':
        hFlag = 1 # 오른손잡이일때는 1
    else:
        hFlag = 0
    fPos = [[3, 0], [3, 2]] # 왼손가락, 오른손가락 좌표
    for num in numbers:
        if num == 1 or num == 4 or num == 7:
            answer += 'L'
            fPos[0] = [num // 3, 0]
        elif num == 3 or num == 6 or num == 9:
            answer += 'R'
            fPos[1] = [(num // 3) - 1, 2]
        else:
            if num == 0:
                ny, nx = 3, 1
            else:
                ny, nx = num // 3, 1
            y1, x1 = fPos[0][0], fPos[0][1]
            y2, x2 = fPos[1][0], fPos[1][1]
            d1, d2 = abs(y1 - ny) + abs(x1 - nx), abs(y2 - ny) + abs(x2 - nx)
            if d1 < d2: # 왼손이 더 가까움
                answer += 'L'
                fPos[0] = [ny, nx]
            elif d1 > d2: # 오른손이 더 가까움
                answer += 'R'
                fPos[1] = [ny, nx]
            else: #같은 거리에 있음
                if hFlag: # 오른손잡이인 경우
                    answer += 'R'
                    fPos[1] = [ny, nx]
                else:
                    answer += 'L'
                    fPos[0] = [ny, nx]
    return answer
