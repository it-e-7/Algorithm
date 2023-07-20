import heapq as hq
def solution(jobs):
    time, answer= 0, 0
    queue, N = [], len(jobs)
    
    hq.heapify(jobs)
    
    while jobs or queue:
        # 도착한 job일 경우 queue에 저장
        while jobs and jobs[0][0] <= time:
            t, burst = hq.heappop(jobs)
            hq.heappush(queue, (burst, t))
        
        # queue는 없는데, jobs는 있을 경우, CPU가 쉬는 시간
        if not queue and jobs:
            time = jobs[0][0]
        else:
            # job 실행 후 요청부터 종료까지 걸린 시간 계산
            t, burst = hq.heappop(queue)
            time += t
            answer += time - burst
    return answer // N

J = [[0, 3], [1, 9], [2, 6]]
print(solution(J))