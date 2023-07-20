import heapq


def solution(jobs):
    answer = 0
    job_count = len(jobs)
    jobs.sort(key=lambda x: x[0])  # 요청 시점 기준으로 정렬
    heap = []
    current_time = 0
    total_response_time = 0

    while jobs or heap:
        while jobs and jobs[0][0] <= current_time:
            request_time, duration = jobs.pop(0)
            # duration을 넣어서 heap을 만들때 duration기준으로
            heapq.heappush(heap, (duration, request_time))

        if heap:
            duration, request_time = heapq.heappop(heap)
            current_time += duration
            total_response_time += (current_time - request_time)

        elif jobs:
            current_time = jobs[0][0]

    answer = total_response_time // job_count
    return answer
