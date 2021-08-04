def solution(board, moves):
    answer = 0
    stack = []
    N = len(board)
    for pos in moves:
        pos = pos - 1
        doll = pickup(board, pos, N)
        if doll > 0:
            stack.append(doll)
            if len(stack) >= 2 and stack[-1] == stack[-2]:
                stack.pop()
                stack.pop()
                answer += 2
    return answer


def pickup(board, pos, N):
    for i in range(N):
        if board[i][pos] > 0:
            doll = board[i][pos]
            board[i][pos] = 0
            return doll
    return 0
