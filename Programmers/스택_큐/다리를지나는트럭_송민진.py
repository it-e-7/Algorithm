from collections import deque

def solution(bridge_length, weight, truck_weights):
    bridge_q = deque([0] * bridge_length)
    truck_q = deque(truck_weights)

    seconds = 0
    crossing_sum = 0
    while truck_q or crossing_sum > 0:
        crossing_sum -= bridge_q.popleft()
        if truck_q:
            checking = truck_q.popleft()
            if crossing_sum + checking <= weight:
                bridge_q.append(checking)
                crossing_sum += checking
            else:
                truck_q.appendleft(checking)
                bridge_q.append(0)
        else:
            bridge_q.append(0)
        seconds += 1

    return seconds

print(solution(2, 10, [7, 4, 5, 6]))
print(solution(100, 100, [10]))
print(solution(100, 100, [10,10,10,10,10,10,10,10,10,10]))