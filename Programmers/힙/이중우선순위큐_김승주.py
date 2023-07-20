import heapq
def solution(operations):
    
    heap = []
    for i in range(len(operations)):
        oper, num = operations[i].split()
        
        if(oper =='I'):
            heapq.heappush(heap, int(num))

        elif oper == 'D' and heap :
            if int(num) ==1:
                heap.pop(-1) # 이거 쓰지 말라했던거 같은뎀...
            else:
                heapq.heappop(heap)
        
    if heap:
        return [max(heap), min(heap)] # 최댓값 최솟값 리턴
    else:
        return [0,0]