def solution(bridge_length, weight, truck_weights):
    answer = 0
    bridge = [0] * bridge_length
    curWeight = 0
    truckIndex = 0
    
    while truckIndex < len(truck_weights):
        curWeight -= bridge[0]
        curTruckWeight = truck_weights[truckIndex]
        if curWeight + curTruckWeight <= weight:
            bridge.append(curTruckWeight)
            curWeight += curTruckWeight
            truckIndex += 1
        else:
            bridge.append(0)
        bridge.pop(0)
        answer += 1
    answer += bridge_length
    return answer