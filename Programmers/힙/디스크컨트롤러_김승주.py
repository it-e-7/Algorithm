import heapq
def solution(jobs):
    answer = 0
    now = 0
    start = -1
    finished_work = 0
    heap = []
    while finished_work < len(jobs):
        for j in jobs:
            if start < j[0] <=now:
                heapq.heappush(heap, [j[1], j[0]]) #작업 소요 시간이 짧은 거 부터 제해야 함. 
        
        if len(heap) > 0 :
            job_x = heapq.heappop(heap)
            start = now 
            now += job_x[0]
            answer += now-job_x[1]  # 종료 시간 - 작업 요청 시간  = 대기 시간 + 작업 시 걸린 시간
            finished_work+=1 # 처리된 작업 개수 증가 
        else: # 처리 가능한 게 없으면 시간만 1초 증가 
            now +=1
    return answer // len(jobs)