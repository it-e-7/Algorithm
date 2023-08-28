from collections import deque

def solution(n, computers):
    answer = 0
    global visited
    visited = [False] * n
    for i in range(n):
        if not visited[i]:
            bfs(i, n, computers)
            answer += 1
    return answer

def bfs(start, n, computers):
    q = deque([start])
    while q:
        com1 = q.popleft()
        for com2 in range(n):
            if computers[com1][com2] == 1 and not visited[com2]:
                visited[com2] = True
                q.append(com2)