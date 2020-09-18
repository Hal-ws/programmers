def solution(phone_book):
    l = len(phone_book)
    phone_book.sorted(key=len)
    answer = True
    for i in range(l - 1):
        lw = len(phone_book[i])
        for j in range(i + 1, l):
            if phone_book[i] == phone_book[j][:lw]:
                return False
    return answer

print(solution(["119", "97674223", "1195524421"]))
