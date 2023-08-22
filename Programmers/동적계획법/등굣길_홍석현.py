# DP
def solution(m, n, puddles):
    matrix = [[0 for i in range(m+1)] for i in range(n+1)]
    matrix[1][1] = 1

    for r in range(1, n+1):
        for c in range(1, m+1):
            if matrix[r][c] == 1:
                # 출발지
                continue
            elif [c, r] in puddles:
                # 잠긴지역
                matrix[r][c] = 0
            else:
                matrix[r][c] = matrix[r-1][c] + matrix[r][c-1]
    return matrix[n][m] % 1000000007


# BFS
from collections import deque

def solution(m, n, puddles):
    answer = 0
    maps = [[0] * m for _ in range(n)]
    maps[0][0] = 1
    q = deque()
    q.append((0, 0))

    while q:
        cx, cy = q.popleft()
        for dx, dy in (0, 1), (1, 0):
            nx, ny = cx + dx, cy + dy
            if 0 <= nx < n and 0 <= ny < m:
                if [ny + 1, nx + 1] in puddles:
                    continue
                maps[nx][ny] += maps[cx][cy]
                if (nx, ny) not in q:
                    q.append((nx, ny))
    answer = maps[n - 1][m - 1] % 1000000007
    return answer