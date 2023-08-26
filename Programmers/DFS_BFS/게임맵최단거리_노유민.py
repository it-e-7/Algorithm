from collections import deque

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]


def BFS(x, y, visited, maps, n, m):
    visited[x][y] = True
    q = deque()
    q.append((x, y))

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if maps[nx][ny] != 0 and not visited[nx][ny]:
                visited[nx][ny] = True
                q.append((nx, ny))
                maps[nx][ny] = maps[x][y] + 1
    return maps[-1][-1] if maps[-1][-1] > 1 else -1


def solution(maps):
    answer = 0
    n = len(maps)
    m = len(maps[0])
    visited = [[False] * m for _ in range(n)]
    answer = BFS(0, 0, visited, maps, n, m)

    return answer
