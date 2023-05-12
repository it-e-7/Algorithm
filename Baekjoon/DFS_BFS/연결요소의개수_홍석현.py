def bfs(start):
    q = []
    q.append(start)
    visited[start] = 1

    while q:
        now = q.pop(0)
        for next in graph[now]:
            if not visited[next]:
                q.append(next)
                visited[next] = 1


N, M = map(int,input().split())
graph = [[]*(N+1) for _ in range(N+1)]
visited = [0] * (N+1)
for i in range(M):
    u,v = map(int,input().split())
    graph[u].append(v)
    graph[v].append(u)

ans = 0
for i in range(1,N+1):
    if not visited[i]:
        bfs(i)
        ans += 1

print(ans)