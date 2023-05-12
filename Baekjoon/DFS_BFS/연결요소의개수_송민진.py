import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

n, m = map(int, input().strip().split())
graph = [[0] * (n+1) for _ in range(n+1)]
visited = [False] * (n+1)

for _ in range(m):
    u, v = map(int, input().strip().split())
    graph[u][v] = 1
    graph[v][u] = 1

def dfs(node):
    new_visit = False
    for i in range(n+1):
        if not visited[i] and graph[node][i] == 1:
            visited[i] = True
            dfs(i)
answer = 0
for j in range(1, n+1):
    if not visited[j]:
        answer += 1
        dfs(j)

print(answer)