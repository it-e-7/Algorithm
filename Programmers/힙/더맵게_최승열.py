import heapq as hq
def solution(scoville, K):
    answer = 0
    hq.heapify(scoville)
    while scoville[0] < K and len(scoville) > 1:
        hq.heappush(scoville, hq.heappop(scoville) + 2 * hq.heappop(scoville))
        answer += 1
    return answer if scoville[0] >= K else -1