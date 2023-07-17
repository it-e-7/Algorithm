def solution(bridge_length, weight, truck_weights):    
    on_bridge = [0] * bridge_length;
    time = 0
    total_weights =0
    while len(on_bridge):
        time +=1
        total_weights -= on_bridge.pop(0)
        if truck_weights:
            if total_weights + truck_weights[0] >  weight : 
                on_bridge.append(0)
            else :
                x = truck_weights.pop(0)
                total_weights += x
                on_bridge.append(x)
    return time

'''
* 5번 테스트 케이스 시간초과 발생
def solution(bridge_length, weight, truck_weights):    
    on_bridge = [0] * bridge_length;
    time = 0
    while len(on_bridge):
        time +=1
        on_bridge.pop(0)
        if truck_weights:
            if sum(on_bridge) + truck_weights[0] >  weight : 
                on_bridge.append(0)
            else :
                on_bridge.append(truck_weights.pop(0))
    return time


'''