from collections import deque


def solution(bridge_length, weight, truck_weights):
    W_onBridge = 0
    waiting = deque()
    curT = 1 # 현재 시간
    for truck in truck_weights:
        waiting.append(truck)
    on_bridge = deque()
    while len(waiting) > 0:
        if W_onBridge + waiting[0] > weight: # 다음 트럭이 탑승 불가능
            while W_onBridge + waiting[0] > weight: # 탑승 가능할때까지 계속 시간 추가함
                tmp = on_bridge.popleft()
                if curT < tmp[2]:
                    curT = tmp[2] # 해당 버스가 다리를 다 건너는 시간에 맞춰 줌
                W_onBridge -= tmp[0]
            on_bridge.append([waiting[0], curT, curT + bridge_length])
            curT = on_bridge[-1][1] + 1
            W_onBridge += waiting[0]
        else: # 바로 탑승가능
            on_bridge.append([waiting[0], curT, curT + bridge_length])
            W_onBridge += waiting[0]
            curT = on_bridge[-1][1] + 1
        waiting.popleft()
    if len(on_bridge) > 0:
        curT = on_bridge[-1][2]
    return curT
