from collections import deque
# 서로소 집합 찾기 - bfs 하나씩 돌면서! 처리! 
def solution(n, computers):
    answer = 0
    visited = [False for _ in range(len(computers))] 
    
    def bfs(i):
        q = deque()
        q.append(i)
        visited[i] = True

        while q:
            index = q.popleft()
            
            for k in range(len(computers[index])):
                if computers[index][k] == 1 and not visited[k] :
                    visited[k] = True
                    q.append(k)
                    
    for i in range(len(computers)):
        if not visited[i] :
            bfs(i)
            answer+=1
    return answer