def solution(participant, completion):
    participant, completion = sorted(participant), sorted(completion)
    l = len(completion)
    answer = None
    for i in range(l):
        if completion[i] != participant[i]:
            answer = participant[i]
            break
    if answer == None:
        answer = participant[l]
    return answer
