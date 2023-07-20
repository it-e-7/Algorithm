import heapq
def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    length = len(scoville)
    while(scoville[0]<K):
        first,second = heapq.heappop(scoville),heapq.heappop(scoville)
        length-=2
        if second ==0:
            return -1
        num = first + (second*2)
        if length==0 and num<K:
            return -1
        heapq.heappush(scoville,num)
        length+=1
        answer+=1
    return answer