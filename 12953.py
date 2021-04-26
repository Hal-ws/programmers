def solution(arr):
    for i in range(1, len(arr)):
        arr[i] = lcd(arr[i - 1], arr[i])
    return arr[-1]


def lcd(a, b):
    return a * b // gcd(a, b)


def gcd(a, b):
    while b != 0:
        r = a % b
        a = b
        b = r
    return a
