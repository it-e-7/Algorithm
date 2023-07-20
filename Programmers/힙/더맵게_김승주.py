# 힙 -:> 파이썬 최소 힙을 지원
import heapq
def solution(scoville, K):
    heapq.heapify(scoville) # 힙 자료구조로 바뀜 
    
    # 스코빌 지수의 길이 2 이상 1000000
    count = 0
    while scoville[0] < K: # 힙의 가장 작은 값이 K 보다 커지면 끝!
        min_first = heapq.heappop(scoville)
        
        if(len(scoville) ==0): # 아무리 합쳐도 모든 음식의 스코빌 지수를 K이상으로 만들 수 없는 경우 ( 다 합쳤는데 K 가 안 넘어요 )
            return -1
        
        min_second = heapq.heappop(scoville)
        
        mixed_scoville = min_first + (min_second * 2 )
        
        heapq.heappush(scoville, mixed_scoville)
        count+=1
    return count