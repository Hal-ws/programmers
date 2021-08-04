def solution(price, money, count):
    answer = (price * count * (count + 1) // 2) - money
    if answer <= 0:
        answer = 0
    return answer
