from collections import deque

def solution(maps):
    bfs((0, 0), maps)
    if maps[len(maps)-1][len(maps[0])-1] == 1:
        return -1
    return maps[len(maps)-1][len(maps[0])-1]

def bfs(start, maps):
    q = deque([start])
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < len(maps) and 0 <= ny < len(maps[0]) and maps[nx][ny] == 1:
                maps[nx][ny] = maps[x][y] + 1
                q.append((nx, ny))

print(solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]))