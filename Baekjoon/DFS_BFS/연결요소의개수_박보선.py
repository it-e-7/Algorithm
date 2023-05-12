import sys
from collections import deque
input = sys.stdin.readline

def bfs(s):
    
    queue = deque([s])
    visited[s] = True
    while queue:
        node = queue.popleft()
        for i in graph[node]:
            if not visited[i]:
                visited[i] = True
                queue.append(i)
        

n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
visited = [False for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
    

c = 0

for i in range(1, n + 1):
    if not visited[i]:
        if not graph[i]:
            c += 1
            visited[i] = True
        else:
            bfs(i)
            c += 1

print(c)