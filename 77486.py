def solution(enroll, referral, seller, amount):
    nameBook = {}
    enroll = ['-'] + enroll
    referral = [None] + referral
    income = [0 for i in range(len(enroll))]
    for i in range(len(enroll)):
        nameBook[enroll[i]] = i
    for i in range(len(seller)):
        dfs(seller[i], amount[i] * 100, income, nameBook, referral)
    return income[1:]


def dfs(name, givenMoney, income, nameBook, referral): #name, givenMoney, income: 받은사람, 받은금액, 총수입
    cIdx = nameBook[name] # 현재 idx
    sndName = referral[cIdx] # 보낼사람의 이름
    income[cIdx] += givenMoney - (givenMoney // 10)
    if sndName == None:
        return
    if givenMoney // 10 > 0:
        dfs(sndName, givenMoney // 10, income, nameBook, referral)
