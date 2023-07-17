from collections import deque

def solution(progresses, speeds):
    answer = []

    q = deque([])
    for idx in range(len(progresses)):
        q.append([progresses[idx], speeds[idx]])

    while q:
        for i in range(len(q)):
            q[i][0] += q[i][1]

        if q[0][0] >= 100:
            q.popleft()
            cnt = 1
            while q:
                now = q.popleft()
                if now[0] >= 100:
                    cnt += 1
                else:
                    q.appendleft(now)
                    break
            answer.append(cnt)

    return answer