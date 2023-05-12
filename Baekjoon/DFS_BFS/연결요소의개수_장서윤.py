import sys

n, m = map(int, input().split())

graph = [[] * n for _ in range(n + 1)]
visited = [False] * (n + 1)
stack = list()

for i in range(m):
    u, v = map(int, sys.stdin.readline().split())

    graph[u].append(v)
    graph[v].append(u)


def dfs():
    ans = 0

    for i in range(1, n + 1):
        if not visited[i]:
            stack.append(i)
            visited[i] = True
            ans += 1

        while stack:
            node = stack.pop()
            for j in graph[node]:
                if not visited[j]:
                    stack.append(j)
                    visited[j]=True
    return ans

print(dfs())
