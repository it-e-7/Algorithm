

'''
방향없는 그래프 -> 연결 요소의 개수 
'''
from collections import deque
import sys
input = sys.stdin.readline


n,m = map(int,input().split())
graph = [[] for _ in range(n+1)]

for _ in range(m):
    u, v = map(int,input().split())
    graph[u].append(v)
    graph[v].append(u)

def bfs(i):
    q = deque([i])
    visited[i] = True

    while q :
        x = q.popleft();
        for i in graph[x]:
            if not visited[i]:
                visited[i]  = True
                q.append(i)  
    


visited = [False]* (n+1)

count = 0
for i in range(1, n+1):
    if not visited[i]:
        if not graph[i]: # 연결된게 없는 경우
            count +=1
            visited[i] = True
        else:
            bfs(i)
            count+=1
print(count)
