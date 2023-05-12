
from collections import deque
n = int(input())

graph =[ list(map(int,input())) for _ in range(n)]

dx = [1,0, -1, 0]
dy = [0, 1, 0, -1]

def bfs(i,j):
    count = 1
    q = deque([(i,j)])
    graph[i][j] = 0

    while q :
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if 0<=nx<n and 0<=ny<n and graph[nx][ny]!=0:
                graph[nx][ny] = 0
                count+=1
                q.append((nx,ny))
    return count

ans =[]
count =0
for i in range(n):
    for j in range(n):
        if graph[i][j]!=0:
            ans.append(bfs(i,j))
            count +=1
print(count)

for i in sorted(ans):
    print(i)