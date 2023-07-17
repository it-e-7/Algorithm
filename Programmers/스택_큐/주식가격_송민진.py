from collections import deque

def solution(prices):
    answer = []
    q = deque(prices)
    while q:
        now = q.popleft()
        seconds = 0
        for pr in q:
            seconds += 1
            if pr < now:
                break
        answer.append(seconds)
    return answer