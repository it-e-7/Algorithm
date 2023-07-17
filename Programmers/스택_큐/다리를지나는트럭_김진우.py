from collections import deque

def solution(bridge_length, weight, truck_weights):
    time = 0
    bridge = deque(0 for _ in range(bridge_length))  # 다리를 나타내는 큐
    truck_weights = deque(truck_weights)  # 대기 중인 트럭을 나타내는 큐
    bridge_weight = 0  # 다리 위의 트럭 무게 합을 나타내는 변수
    print(f'bridge, truck_weights : {bridge, truck_weights}')

    while bridge:
        time += 1
        bridge_weight -= bridge.popleft()  # 다리에서 트럭이 지나감

        if truck_weights:
            if bridge_weight + truck_weights[0] <= weight:
                truck = truck_weights.popleft()  # 대기 중인 트럭을 다리로 올림
                bridge.append(truck)
                bridge_weight += truck
            else:
                bridge.append(0)  # 대기 중인 트럭을 다리에 올리지 못하면 0을 추가

    return time

bridge_length = 2
weight = 10
truck_weights = [7,4,5,6]

solution(bridge_length, weight, truck_weights)