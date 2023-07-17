from collections import deque


def solution(bridge_length, weight, truck_weights):
    answer = 0
    bridge_weight = 0

    bridge = deque([0 for _ in range(bridge_length)])
    truck = deque(truck_weights)

    while truck or bridge:
        answer += 1
        bridge_weight -= bridge.popleft()

        if truck:
            w = truck.popleft()
            bridge_weight += w
            if bridge_weight <= weight:
                bridge.append(w)

            else:
                bridge_weight -= w
                truck.appendleft(w)
                bridge.append(0)

    return answer
