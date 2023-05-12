def bfs(si,sj):
    q = []
    apart = 1
    q.append((si,sj))
    visited[si][sj] = 1

    while q:
        ci,cj = q.pop(0)

        for di,dj in (-1,0),(1,0),(0,1),(0,-1):
            ni,nj = ci+di, cj+dj
            if 0<=ni<N and 0<=nj<N and not visited[ni][nj] and arr[ni][nj] == 1:
                q.append((ni,nj))
                visited[ni][nj] = 1
                apart += 1
    return apart


N = int(input())
arr = [list(map(int,input())) for _ in range(N)]
visited = [[0]*N for _ in range(N)]


aparts = []
apart = 0
for si in range(N):
    for sj in range(N):
        if arr[si][sj] == 1 and not visited[si][sj]:
            cnt = bfs(si,sj)
            aparts.append(cnt)
            apart += 1

aparts.sort()
print(apart)
for i in aparts:
    print(i)